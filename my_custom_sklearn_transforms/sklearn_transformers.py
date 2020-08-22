import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin



# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()

        #We create a holder data without the columns
        holder = data.drop(labels=self.columns, axis='columns')

        #Pass the imputer
        si = SimpleImputer(
            missing_values=np.nan,  # los valores que faltan son del tipo ``np.nan`` (Pandas estándar)
            #strategy='constant',  # la estrategia elegida es cambiar el valor faltante por una constante
            #fill_value=0,  # la constante que se usará para completar los valores faltantes es un int64 = 0
            #verbose=0,
            copy=True,
            strategy='mean'
        )

        si.fit(X=holder)

        df_data_3 = pd.DataFrame.from_records(
            data=si.transform(
                X=holder
            ),  
            columns=self.columns
        )


        #Re add the profile col
        df_data_3.insert(12,'PROFILE',df_data_1['PROFILE'], True)

        # Retornamos um novo dataframe sem as colunas indesejadas
        return df_data_3
