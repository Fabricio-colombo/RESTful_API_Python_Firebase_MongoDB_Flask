from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "Books"
COLLECTION_NAME = "Non-Fiction"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Define routes and API endpoints here
@app.route('/')
def bem_vindo():
    return "Bem-vindo à API de Livros! Esta é uma API para consultar livros que são de não ficção em um banco de dados MongoDB."

@app.route('/livros', methods=['GET'])
def get_all_books():
    livros = list(collection.find({}))
    return jsonify({'livros': livros})

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
