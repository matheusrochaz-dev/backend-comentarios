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
            comentarios = f.read()
    except FileNotFoundError:
        comentarios = "Nenhum comentário ainda."
    
    return jsonify({"comentarios": comentarios})

@app.route('/comentar', methods=['POST'])
def comentar():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        with open(ARQUIVO_COMENTARIOS, "a", encoding="utf-8") as f:
            f.write(comentario + "\n\n")
    return jsonify({"message": "Comentário adicionado com sucesso!"}), 201


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
