
import numpy as np
import pandas as pd


class Utils: 


    def load_from_csv(self, file)->pd.DataFrame:

        df = pd.read_csv(file)
        return df 

    def load_from_excel(self, file)->pd.DataFrame:

        df = pd.read_excel(file)
        return df 

    def drop_duplicates(self, file: pd.DataFrame)->pd.DataFrame: 

        df = file.drop_duplicates()
        return df 

    def extracting_features(self, df: pd.DataFrame) -> np.array: 

        X = df.drop(["Glucose", "Acetate"])
        y = df.loc[:, ["Glucose", "Acetate"]]
        return X, y
    


    



