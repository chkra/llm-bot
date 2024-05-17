#imports
from flask import Flask, render_template, request
#from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from openai import OpenAI


from llama_index.core.node_parser import SimpleNodeParser
import os

with open('api_key', 'r') as file:
    api_key = file.read().strip()
os.environ['OPENAI_API_KEY'] = api_key

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

app = Flask(__name__)

#create chatbot
documents = SimpleDirectoryReader('data').load_data()
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)


DUMMY_EXAMPLE = "\#javascript "\
 + "function mycode() { "\
 + "var nColumns = datatable[0].length; "\
 + "var nRows = datatable.length; "\
 + "var sum = 0; "\
 + "var n = 0; "\
 + "for (r=0; r<nRows; r++) { "\
 + "n++; "\
 + "sum = sum + datatable[r][2]; " \
 + "} "\
 + "var tmp=sum/n; "\
 + "var answer = \"The average of the numbers in the third column is \" + tmp.toString() ;"\
 + "return answer; "\
+ "}"\
+ "mycode();"\
+ "\#"

QAexamples = []  #Array of example requests and corresponding javascript code
QAexamples.append( {"role": "system", \
"content": "\n\nYou are an expert data analyst and programmer assistant who translates a users request into JavaScript code, providing the code between \#javascript and \# and embedding it into a function called mycode(). Here you are working on a data table called datatable of size nRows rows times nColumns columns. Given the users request you reply with JavaScript code to process the corresponding numbers of the table, and with what function. Take into account the fact that columns of a data table appear on the second index of a javascript array." \
+ "For example, if the user asks What is the average of the numbers in the third column? you return this code: " \
+ DUMMY_EXAMPLE })
 
 
columnNames = "A  B  C\n" 
rowNames = "x y z"
nRows = 3
datatable = \
        columnNames \
    +   "1  2  3\n" \
    +   "4  5  6\n" \
    +   "7  8  9\n" \
    

def handleUserInput(user_input):

    user_prompt = "Given an array called datatable which has nColumns columns (of names " + columnNames + ") and " \
                        + str(nRows) +" rows (of names " + rowNames + "):\n\n" \
                        + user_input \
                        + "\n\nWrite only one single complete piece of Javascript code.\n\n" \
                        + "The script must finish by returning the full answer to the question as a string."

    fullprompt = [];

    for example in QAexamples:
        fullprompt.append(example)

    fullprompt.append({"role": "user", "content": user_input})
    return fullprompt;

def extractJsCode(response):
    start_marker = "\\#javascript"
    end_marker = "\\#"

    if start_marker in response and end_marker in response:
        substring = response.split(start_marker, 1)[1].split(end_marker, 1)[0]
    else:
        substring = ""

    return(substring)


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

@app.route("/analysis/")
def analysis():
    return render_template("analysis.html")

@app.route("/get/")
def get_bot_response():
    # chatbot is set in service context
    userText = request.args.get('msg')
    query_engine = index.as_query_engine(response_mode="simple_summarize", verbose=True)
    response = query_engine.query(userText)
    return str(response)

@app.route("/get_analysis")
def get_analysis_bot_response():
    userText = request.args.get('msg')
    prompt = handleUserInput(userText)

    chat_completion = client.chat.completions.create( messages=prompt, model="gpt-3.5-turbo")
    response = chat_completion.choices[0].message.content
    # response = DUMMY_EXAMPLE
    response = extractJsCode(response)
    return str(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
