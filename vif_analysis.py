# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:07:52 2021

@author: MIKLOS
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor


def calc_reg_return_vif(X, y):
    """
    Utility function to calculate the VIF. This section calculates the linear
    regression inverse R squared.

    Parameters
    ----------
    X : DataFrame
        Input data.
    y : Series
        Target.

    Returns
    -------
    vif : float
        Calculated VIF value.

    """
    X = X.values
    y = y.values

    if X.shape[1] == 1:
        print("Note, there is only one predictor here")
        X = X.reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    vif = 1 / (1 - reg.score(X, y))

    return vif


def calc_vif_from_scratch(df):
    """
    Calculating VIF using function from scratch

    Parameters
    ----------
    df : DataFrame
        without target variable.

    Returns
    -------
    vif : DataFrame
        giving the feature - VIF value pair.

    """

    vif = pd.DataFrame()

    vif_list = []
    for feature in list(df.columns):
        y = df[feature]
        X = df.drop(feature, axis="columns")
        vif_list.append(calc_reg_return_vif(X, y))
    vif["feature"] = df.columns
    vif["VIF"] = vif_list
    return vif


def calc_vif(df):
    """
    Calculating VIF using variance_inflation_factor from
    statsmodels.stats.outliers_influence

    Parameters
    ----------
    df : DataFrame
        without target variable.

    Returns
    -------
    vif : DataFrame
        giving the feature - VIF value pair.

    """
    vif = pd.DataFrame()
    vif["feature"] = df.columns
    vif["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]

    return vif


if __name__ == "__main__":
    df_ = pd.read_csv("titanic-data.csv")
    # print(df.columns)
    df_ = df_[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]

    # male -> 0, female -> 1
    df_["Sex"] = np.where(df_["Sex"] == "male", 0, 1)

    # drop missing value rows
    df_ = df_.dropna()
    df_.drop(["Survived"], axis=1, inplace=True)

    # wrong!!
    print("\nStatsmodel VIF\n")
    print(calc_vif(df_))

    print("\n----------\n")

    # Right!
    # Chad way to do it!
    print("Chad VIF (comparable to the R implementation)\n")
    print(calc_vif_from_scratch(df_))
