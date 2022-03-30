from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    return int(requests.get('http://addition:5051/'+str(n1)+'/'+str(n2)).text)

def minus(n1, n2):
    return int(requests.get('http://subtraction:5052/'+str(n1)+'/'+str(n2)).text)

def multiply(n1, n2):
    return int(requests.get('http://multiplication:5053/'+str(n1)+'/'+str(n2)).text)

def divide(n1, n2):
    return int(requests.get('http://division:5054/'+str(n1)+'/'+str(n2)).text)

def lcm(n1, n2):
    return int(requests.get('http://lcm:6009/'+str(n1)+'/'+str(n2)).text)

def exponent(n1, n2):
    return requests.get('http://exponent:5057/'+str(n1)+'/'+str(n2)).text

def greatest(n1, n2):
    return requests.get('http://greatest:5058/'+str(n1)+'/'+str(n2)).text


@app.route('/', methods=['POST', 'GET'])
def index():
    # Handle None type exception and get first and second number
    try:
        # Check if entered string is a number or not
        number_1 = int(request.form['first'])
        number_2 = int(request.form['second'])
        operation = request.form.get('operation')
    except:
        number_1=0
        number_2=0
        return render_template('index.html', result=None)
    result = None
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
    elif operation == 'lcm':
        result = lcm(number_1, number_2)
    elif operation == 'exponent':
        result = exponent(number_1, number_2)
    elif operation == 'greatest':
        result = greatest(number_1, number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )