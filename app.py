import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API do Watson Assistant
watson_api_key = os.getenv('WATSON_API_KEY')  # Carrega a chave da API a partir das variáveis de ambiente
watson_url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/v2/assistants/c6aabe50-9141-4f22-ba88-11e236849fd9/sessions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {watson_api_key}',
}

# Função para enviar uma mensagem ao Watson Assistant
def send_message_to_watson(message):
    data = {
        'input': {
            'text': message
        }
    }
    response = requests.post(watson_url, headers=headers, data=json.dumps(data))
    return response.json()

# Configurações da API Flask para o modelo treinado
flask_api_url = 'http://127.0.0.1:5000/prever'  # Altere se necessário

# Função para obter previsão do modelo
def get_prediction(data):
    response = requests.get(flask_api_url, params=data)
    return response.json()

# Interface do Streamlit
st.title("Sistema de Diagnóstico Automotivo")

# Entrada do usuário para dados do carro
pressao_liquido_arrefecimento = st.number_input("Pressão do líquido de arrefecimento")
temperatura_liquido_arrefecimento = st.number_input("Temperatura do líquido de arrefecimento")
rpm_motor = st.number_input("RPM do motor")
pressao_combustivel = st.number_input("Pressão do combustível")
pressao_oleo_lubrificante = st.number_input("Pressão do óleo lubrificante")
temperatura_oleo_lubrificante = st.number_input("Temperatura do óleo lubrificante")

if st.button("Fazer Previsão"):
    prediction_data = {
        'pressao_liquido_arrefecimento': pressao_liquido_arrefecimento,
        'temperatura_liquido_arrefecimento': temperatura_liquido_arrefecimento,
        'rpm_motor': rpm_motor,
        'pressao_combustivel': pressao_combustivel,
        'pressao_oleo_lubrificante': pressao_oleo_lubrificante,
        'temperatura_oleo_lubrificante': temperatura_oleo_lubrificante
    }
    prediction = get_prediction(prediction_data)
    st.write(f"Previsão: {prediction}")

# Campo de texto para interação com o Watson Assistant
user_message = st.text_input("Digite sua mensagem para o Assistente:")
if st.button("Enviar"):
    watson_response = send_message_to_watson(user_message)
    st.write(f"Resposta do Assistente: {watson_response['output']['generic'][0]['text']}")
