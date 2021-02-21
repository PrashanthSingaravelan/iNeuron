from flask import Flask, request
app = Flask(__name__)       ## Creating a flask object

@app.route("/about")
def hello():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)