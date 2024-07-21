from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return {"response": response}

def chatbot_response(user_input):
    # Implement your chatbot logic here
    # For demonstration, let's echo the user's input
    return user_input

if __name__ == "__main__":
    app.run(debug=True)
