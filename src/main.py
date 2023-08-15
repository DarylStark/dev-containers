from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def root() -> str:
    return 'Hallo\n'


@app.route('/info')
def info() -> str:
    return 'Information about the project\n'


@app.get('/hello/<string:world>')
def daryl(world: str) -> str:
    return f'Hello {world.capitalize()}!\n'


@app.get('/joke')
def get_dad_joke() -> str:
    api_request = requests.get(
        url='https://icanhazdadjoke.com',
        headers={
            'Accept': 'application/json',
            'User-Agent': 'Daryl API testing (https://github.com/EngineerDaryl)'
        })
    joke = api_request.json()
    return f'Joke "{joke["joke"]}"\n'
