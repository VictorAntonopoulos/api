from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar o modelo treinado (substitua o caminho pelo caminho do seu arquivo)
modelo = joblib.load('modelo_treinado.joblib')

# Definindo a rota inicial
@app.route('/')
def home():
    return "API está rodando!"

@app.route('/prever', methods=['GET'])
def prever():
    try:
        # Pegue os parâmetros da query string
        engine_rpm = float(request.args.get('engine_rpm'))
        lub_oil_pressure = float(request.args.get('lub_oil_pressure'))
        fuel_pressure = float(request.args.get('fuel_pressure'))
        coolant_pressure = float(request.args.get('coolant_pressure'))
        lub_oil_temp = float(request.args.get('lub_oil_temp'))
        coolant_temp = float(request.args.get('coolant_temp'))

        # Crie um DataFrame com os nomes das features
        dados = pd.DataFrame([[engine_rpm, 
                               lub_oil_pressure, 
                               fuel_pressure, 
                               coolant_pressure, 
                               lub_oil_temp, 
                               coolant_temp]],
                             columns=['Engine rpm', 
                                      'Lub oil pressure', 
                                      'Fuel pressure', 
                                      'Coolant pressure', 
                                      'lub oil temp', 
                                      'Coolant temp'])

        # Faz a predição com o modelo treinado
        previsao = modelo.predict(dados)

        # Retorne o resultado em formato JSON
        return jsonify({'previsao': int(previsao[0])})
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
