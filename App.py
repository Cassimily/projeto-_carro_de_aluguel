import streamlit as st 
st.title('Mmotors - Aluguel de Carros')
st.subheader('Loja de Carros....')
st.sidebar.title("Escolha um Modelo")
st.sidebar.image('logo.png')


carros = ['BMW','Volkswagem', 'Porsche', 'Toyota']

opção = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


st.image(f'{opção}.png')
st.markdown(f'## Voce alugou o modelo: {opção}')
st.markdown('---')
