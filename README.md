# House_Price_Predictor_For_YT
- After analysisng the dataset we can see that their are 7 features and 1 outcome column which is sale price.
- Extract the Sale Price column and store it in y for actual outcomes.
- Create feature_names for all features and store all the features.
- Their are multiple features thus we first try to use decision tree regressor to predict the out come.
- First try to predict the house prices using the defaults of Decision Tree Regressor with a random state 1 for model reproducibility.
- Then we check the mean absolute error
- Now we have to reduce this error thus we will keep changing the no of leaf nodes and check in which we are getting the minimum error.
- After finding the best no of leaf nodes we can predict the prices of the house.
