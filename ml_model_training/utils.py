
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

        X_glucose = df.loc[:, "920.07"]
        X_acetate = df.loc[:, ["1060.19", "1119.87"]]
        y_glucose = df.loc[:, "Glucose"]
        y_acetate = df.loc[:, "Acetate"]

        return np.array(X_glucose), np.array(X_acetate), np.array(y_glucose), np.array(y_acetate)
    


    



