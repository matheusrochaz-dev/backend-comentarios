from flask import Flask, request, jsonify
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app, origins=["https://front-comentarios.vercel.app"])  
ARQUIVO_COMENTARIOS = "comentarios.txt"

@app.route('/comentarios', methods=['GET'])
def obter_comentarios():
    try:
        with open(ARQUIVO_COMENTARIOS, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            comentarios = conteudo.split("\n\n") if conteudo else []
    except FileNotFoundError:
        comentarios = []

    return jsonify({"comentarios": comentarios})

@app.route('/comentarios', methods=['POST'])
def adicionar_comentario():
    data = request.get_json()
    comentario = data.get("comentario", "").strip()

    if not comentario:
        return jsonify({"erro": "Comentário vazio"}), 400

    with open(ARQUIVO_COMENTARIOS, "a", encoding="utf-8") as f:
        f.write(comentario + "\n\n")

    return jsonify({"mensagem": "Comentário salvo com sucesso!"}), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
