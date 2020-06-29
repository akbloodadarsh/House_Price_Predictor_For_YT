import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


# without using in-sample data
# Path of the file to read
iowa_file_path = 'train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
# Create the list of features below
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)
predictions = iowa_model.predict(X)

#mean absolute error
print(mean_absolute_error(y, predictions))

#with using in-sample data

train_X,test_X,train_y,test_y = train_test_split(X, y, random_state = 0) 
iowa_model = DecisionTreeRegressor(random_state=0)
iowa_model.fit(train_X,train_y)
predictions = iowa_model.predict(test_X)
print(mean_absolute_error(test_y,predictions))

# Write loop to find the ideal tree size from candidate_max_leaf_nodes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
best_mae = float('inf')
best_tree_size = 0
for max_leaf_nodes in candidate_max_leaf_nodes:
    mae = get_mae(max_leaf_nodes, train_X, test_X, train_y, test_y)
    if mae < best_mae:
        best_mae = mae
        best_tree_size = max_leaf_nodes
        
# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size)

# fit the final model and uncomment the next two lines
final_model.fit(X,y)
predictions = final_model.predict(X)
print(mean_absolute_error(y,predictions))
