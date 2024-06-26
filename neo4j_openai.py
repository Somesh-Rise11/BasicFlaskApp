from flask import Flask, jsonify, request
from neo4j import GraphDatabase
import openai

app = Flask(__name__)

neo4j_uri = "neo4j+s://d85d49e5.databases.neo4j.io"
neo4j_user = "neo4j"
neo4j_password = "neo4j_pass"

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

openai.api_key = 'your_openai_api_key_here'

@app.route('/')
def home():
    return "Welcome to Neo4j Aura Flask App!"

@app.route('/nodes', methods=['GET'])
def get_nodes():
    query = "MATCH (n) RETURN n LIMIT 25"
    with driver.session() as session:
        result = session.run(query)
        nodes = [serialize_node(record['n']) for record in result]
    return jsonify(nodes)

@app.route('/ask_openai', methods=['POST'])
def ask_openai():
    question = request.json['question']

    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )

    return jsonify({"answer": response.choices[0].text.strip()})

def serialize_node(node):
    return {
        "id": node.id, 
        "labels": list(node.labels),
        **dict(node)   
    }

if __name__ == '__main__':
    app.run(debug=True)
