import streamlit as st 
import requests
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API do Watson Assistant
watson_api_key = os.getenv('WATSON_API_KEY')
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

# Interface do Streamlit
st.set_page_config(page_title="Chatbot Galdí", layout="wide")
st.title("🌟 Chatbot Galdí 🌟")
st.markdown("Olá! Eu sou Galdí, seu assistente virtual. Como posso ajudar você hoje?")

# Estilo para o campo de entrada
user_message = st.text_input("Digite sua mensagem para Galdí:", placeholder="Escreva aqui...")

if st.button("Enviar"):
    if user_message:
        with st.spinner("Galdí está pensando..."):
            watson_response = send_message_to_watson(user_message)
            response_text = watson_response['output']['generic'][0]['text']
            st.success(f"Galdí: {response_text}")
    else:
        st.warning("Por favor, digite uma mensagem antes de enviar.")

# Espaço para feedback ou interações adicionais
st.sidebar.header("💬 Interações Adicionais")
st.sidebar.markdown("Você pode fazer perguntas sobre:")
st.sidebar.markdown("- Problemas automotivos")
st.sidebar.markdown("- Manutenção de veículos")
st.sidebar.markdown("- Dicas gerais de automóveis")
