import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'status': 'OK'}

@app.route(f'/.well-known/acme-challenge/{os.environ.get("ACME_CHALLENGE_URL_KEY")}')
def acme_challenge():
    return os.environ.get("ACME_CHALLENGE_RESPONSE")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
