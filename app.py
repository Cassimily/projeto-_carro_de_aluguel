
import streamlit as st



 #---------------------------- Sidebar
st.sidebar.image("logo.png")
st.sidebar.title("Nox Auto Club - Aluguel de carros🚗")
carros = ["Pagani Huayra", "Toyota Supra Skyline", "Mazda RX-7","Acura NSX"]
carro= st.sidebar.selectbox("Escolha seu carro: ", carros)


#-------------------------------Body
st.title("Nox Auto Club - Aluguel de carros🚗")
st.image(f"{carro}.png")
st.write(f"voce alugou o {carro}")

dias = st.text_input(f"Por quantos dias voce alugou o {carro}?")
km = st.text_input(f"Quantos km você rodou com o {carro}?")

if carro == "Pagani Huayra":
    diaria = 55000

elif carro == "Toyota Supra Skyline":
    diaria = 600000

elif carro == "Mazda RX-7":
    diaria = 500000

elif carro == "Acura NSX":
    diaria = 600000


if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total = (dias * diaria) + (km * 0.15)

    st.warning(f"O total do aluguel a se pagar é R${total}.")    