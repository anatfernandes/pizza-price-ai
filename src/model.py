import pandas as pd
from sklearn.linear_model import LinearRegression


class AIModel:
    def __init__(self):
        self.model = None
        self.load_data()
        self.fit()

    def load_data(self):
        self.df = pd.read_csv("pizzas.csv")

    def fit(self):
        if self.model:
            return

        self.model = LinearRegression()

        x = self.df[["diametro"]]
        y = self.df[["preco"]]

        self.model.fit(x, y)

    def predict(self, diameter):
        x_predict = pd.DataFrame([[diameter]], columns=["diametro"])
        return self.model.predict(x_predict)[0][0]
