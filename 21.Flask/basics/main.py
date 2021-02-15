from flask import Flask, requests
app = Flask(__name__)

@app.route("/about")
def hello():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)