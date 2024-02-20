#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    string = ''
    for i in range(0, parameter):
        string+=f'{str(i)}\n'
    return string

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == "+":
        total = int(num1) + int(num2)
        return str(total)
    elif operation == "-":
        total = int(num1) - int(num2)
        return str(total)
    elif operation == "*":
        total = int(num1) * int(num2)
        return str(total)
    elif operation == "div":
        total = int(num1) / int(num2)
        return str(total)
    elif operation == "%":
        total = int(num1) % int(num2)
        return str(total)