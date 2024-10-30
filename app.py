import streamlit as st
import requests

# Defina a URL da sua API
API_URL = "http://127.0.0.1:5000/prever"



# Título da aplicação
st.title("Previsão de Dados do Veículo")

# Campos para entrada de dados com tradução
motor_rpm = st.number_input("RPM do Motor", min_value=0.0)
lub_oil_pressao = st.number_input("Pressão do Óleo Lubrificante", min_value=0.0)
pressao_combustivel = st.number_input("Pressão do Combustível", min_value=0.0)
pressao_refrigerante = st.number_input("Pressão do Refrigerante", min_value=0.0)
lub_oil_temp = st.number_input("Temperatura do Óleo Lubrificante", min_value=0.0)
temperatura_refrigerante = st.number_input("Temperatura do Refrigerante", min_value=0.0)

# Botão para fazer a previsão
if st.button("Fazer Previsão"):
    # Prepare os dados para enviar à API
    data = {
        "engine_rpm": motor_rpm,
        "lub_oil_pressure": lub_oil_pressao,
        "fuel_pressure": pressao_combustivel,
        "coolant_pressure": pressao_refrigerante,
        "lub_oil_temp": lub_oil_temp,
        "coolant_temp": temperatura_refrigerante
    }

    # Envie uma requisição GET para a API
    response = requests.get(API_URL, params=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Previsão: {result['previsao']}")
    else:
        st.error(f"Erro: {response.json()['erro']}")
