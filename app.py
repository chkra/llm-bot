#imports
from flask import Flask, render_template, request
#from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from llama_index.node_parser import SimpleNodeParser
import os

os.environ['OPENAI_API_KEY'] = "your api key here"


app = Flask(__name__)

#create chatbot
documents = SimpleDirectoryReader('htw-data').load_data()
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(documents)
index = GPTVectorStoreIndex(nodes)

#define app routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    response = index.query(userText)
    return str(response)

if __name__ == "__main__":
    app.run()

