from flask import Flask
app = Flask(__name__)

def mkbold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def mkitalic(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Cute kitten gif</p>' \
           '<img src="https://media.giphy.com/media/6uMqzcbWRhoT6/giphy.gif" width=700px>'

@app.route('/bye')
@mkbold
@mkitalic
def say_bye():
    return 'Bye!'

@app.route('/<name>')
def greet(name):
    return f'Hello {name}!'

if __name__ == "__main__":
    app.run(debug=True)