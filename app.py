from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Tool Renting Website - Home Page"

if __name__ == '__main__':
    app.run(debug=True)

