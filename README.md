# Variance-Inflation-Factor-VIF-
## Variance Inflation Factor in Python &amp; R

A way to explore the relationship between the features is to check the **Variance Inflation Factor (VIF)**. The VIF measures the correlation among independent variables (predictors) in regression models. We refer to this type of correlation as multicollinearity. Excessive multicollinearity can cause problems for regression models. The steps of VIF analysis are as follows:
1.	Drop target variable
2.	Select one feature as new target,
3.	Use predictor features to predict new target using a linear regression model,
4.	Calculate R^2, (R squared is a measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model), then calculate vif= 1/(1-R^2)
5.	Repeat steps 1-3 for all features

A VIF greater than 10 is a signal that the model has a collinearity problem.

I've noticed that the variance_inflation_factor library from from statsmodels.stats.outliers_influence gives different results for the VIF than the vif function from the R car library.

The **vif_analysis.py** file contains the *calc_vif* function which calculates the VIF using the statsmodels implementation, while vif_analysis.R contains the R implementation. Printing out the outputted dataframes (using the tatinic dummy data) show that there is indeed a difference between the outputs.

The **vif_analysis.py** file contains also a *calc_vif_from_scratch* function, which uses a LinearRegression model to calculate the VIF. The output of this function is the same as the output of the R implementation.

Enjoy!
