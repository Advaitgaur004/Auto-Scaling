from flask import Flask
app = Flask(__name__)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@app.route('/')
def assignment2():
    product = factorial(1000)
    return f'Factorial of 1000 is : {product}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)