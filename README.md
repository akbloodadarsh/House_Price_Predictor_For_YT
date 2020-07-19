# House_Price_Predictor_For_YT

- We extract the Sale Price column and store it in y for actual outcomes.
- Then after analysisng the data we can see that their are 7 features.
- we create feature_names for all features.
- We first try to predict the house prices using the defaults of Decision Tree Regressor with a random state 1 for model reproducibility.
- Then we check the mean absolute error
- Now we have to reduce this error thus we will keep changing the no of leaf nodes and check in which we are getting the minimum error.
- After finding the best no of leaf nodes we can predict the prices of the house.
