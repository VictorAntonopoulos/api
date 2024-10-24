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

    # Verifica se a resposta está no formato esperado
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao se comunicar com o assistente. Verifique a chave da API e a URL.")
        return {}

# Interface do Streamlit
st.set_page_config(page_title="Chatbot Galdí", layout="wide")
st.title("🌟 Chatbot Galdí 🌟")
st.markdown("Olá! Eu sou Galdí, seu assistente virtual. Como posso ajudar você hoje?")

# Campo de texto para interação com o Watson Assistant
user_message = st.text_input("Digite sua mensagem para Galdí:", placeholder="Escreva aqui...")

if st.button("Enviar"):
    if user_message:
        with st.spinner("Galdí está pensando..."):
            watson_response = send_message_to_watson(user_message)

            # Verifica se a resposta contém o texto esperado
            if 'output' in watson_response and 'generic' in watson_response['output']:
                response_text = watson_response['output']['generic'][0].get('text', 'Desculpe, não consegui entender a resposta.')
                st.success(f"Galdí: {response_text}")
            else:
                st.error("Desculpe, não consegui processar a resposta do assistente.")
    else:
        st.warning("Por favor, digite uma mensagem antes de enviar.")
