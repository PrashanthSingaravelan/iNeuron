from flask import Flask, render_template, request, jsonify
app = Flask(__name__)   ## Creating a flask object

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')  ## home page will go to index.html

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        ## Getting the input from the index.html to app.py
        operation = request.form['operation_html']
        num1 = int(request.form['num1_html'])
        num2 = int(request.form['num2_html'])
        if(operation=='add'):
            r = num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)

        # Going to result.html page with result-value
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation = request.json['operation_post']
        num1 = int(request.json['num1_post'])
        num2 = int(request.json['num2_post'])
        if(operation=='add'):
            r = num1 + num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)   ## result in-terms of json


if __name__ == '__main__':
    app.run(debug=True)
