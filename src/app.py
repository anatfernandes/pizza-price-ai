import streamlit as st

from .model import AIModel

first_time = True


class App:
    def __init__(self):
        global first_time
        self.first_time = first_time
        self.model = AIModel()

    def run(self):
        st.title("Prevendo o preço de uma pizza")
        st.divider()

        diameter = st.number_input(
            "Digite o tamanho do diâmetro da pizza: ", min_value=0
        )

        if diameter:
            price = self.predict_price(diameter)

            st.success(
                f"O valor da pizza com diâmetro de {diameter:.2f}cm é de R$ {price:.2f}."
            )

            if self.first_time:
                self.handle_first_time()
        elif not self.first_time:
            st.warning("Informe um tamanho acima de 0cm!")

    def handle_first_time(self):
        global first_time
        first_time = False
        st.balloons()

    def predict_price(self, diameter):
        return self.model.predict(diameter)
