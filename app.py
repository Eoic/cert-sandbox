import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'status': 'OK'}

@app.route(f'/.well-known/acme-challenge/{os.environ.get("ACME_CHALLENGE_URL_KEY")}')
def acme_challenge():
    return os.environ.get("ACME_CHALLENGE_RESPONSE")