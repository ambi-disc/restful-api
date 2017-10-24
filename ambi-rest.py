from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/account/create')
def create_account_endpoint():
    return jsonify(
        success=True,
        authToken="aTHN45nthuoe43+?",
        timeoutTimestamp="1635094775"
    )


@app.route('/account/login')
def login_endpoint():
    return jsonify(
        success=True,
        authToken="aTHN45nthuoe43+?",
        timeoutTimestamp="1635094775"
    )


@app.route('/account/verify_token')
def verify_token_endpoint():
    return jsonify(
        valid=True
    )

db = None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
