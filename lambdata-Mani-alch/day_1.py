"""Implement at least 2 of the following "helper" utility functions"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import shap


class Manis_alchemy:
    """class for my two hjelper funtions"""

    def __init__(self):
        pass


    def splitter(self, df):
        """function splits a dataframe"""
        df = df.copy() #protectg og dataframe
        train, test = train_test_split(df, 
                                            train=.8,
                                            test=.2)

        X = train
        y = test
        return X, y

    def shap_val(self, row, model, encoder):
        """Function returns shap values"""
        row = X_test.loc[[row]]
        row

        explainer = shap.TreeExplainer(model)
        encoder = encoder
        row_processed = encoder.transform(row)
        shap_values = explainer.shap_values(row_processed)

        shap.initjs()
        return shap.force_plot(
            base_value=explainer.expected_value,
            shap_values=shap_values,
            features=row,
            link='logit')
    
        