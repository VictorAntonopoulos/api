import streamlit as st
import requests

# Defina a URL da sua API
API_URL = "http://127.0.0.1:5000/prever"

# Título da aplicação
st.title("Previsão de Dados do Veículo")

# Campos para entrada de dados
engine_rpm = st.number_input("Engine RPM", min_value=0.0)
lub_oil_pressure = st.number_input("Lub Oil Pressure", min_value=0.0)
fuel_pressure = st.number_input("Fuel Pressure", min_value=0.0)
coolant_pressure = st.number_input("Coolant Pressure", min_value=0.0)
lub_oil_temp = st.number_input("Lub Oil Temperature", min_value=0.0)
coolant_temp = st.number_input("Coolant Temperature", min_value=0.0)

# Botão para fazer a previsão
if st.button("Fazer Previsão"):
    # Prepare os dados para enviar à API
    data = {
        "engine_rpm": engine_rpm,
        "lub_oil_pressure": lub_oil_pressure,
        "fuel_pressure": fuel_pressure,
        "coolant_pressure": coolant_pressure,
        "lub_oil_temp": lub_oil_temp,
        "coolant_temp": coolant_temp
    }

    # Envie uma requisição GET para a API com os dados como parâmetros
    response = requests.get(API_URL, params=data)

    # Verifique a resposta da API
    if response.status_code == 200:
        result = response.json()
        st.success(f"Previsão: {result['previsao']}")
    else:
        st.error(f"Erro: {response.json().get('erro', 'Erro desconhecido')}")
