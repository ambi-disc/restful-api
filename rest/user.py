import calendar
import datetime

from flask import jsonify


def create_account(request):
    first = request.get_json()['firstName']
    last = request.get_json()['lastName']
    email = request.get_json()['emailAddress']
    profession = request.get_json()['profession']
    password = request.get_json()['password']
    hash = "blahblahblah"
    # TODO make hash, hash pword

    token = "blah"
    token_timeout = "5529085890253890"
    # todo make tokens

    if email_in_db(email):
        return jsonify(
            success=False,
            errorMessage="User already exists with specified email"
        )

    csr = db.curser()
    query = ("INSERT INTO users (firstName, lastName, emailAddress, profession, password, hash, token, tokenTimeout) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    csr.execute(query, (first, last, email, profession, password, hash, token, token_timeout))

    return jsonify(
            success=True,
            authToken=token,
            timeoutTimestamp=token_timeout
        )


def email_in_db(email):
    pass # TODO


def login(request):
    email = request.get_json()['emailAddress']
    password = request.get_json()['password']

    # TODO hash pword with hash from db

    token = "blah"
    token_timeout = "5529085890253890"
    # todo make tokens

    csr = db.curser()
    query = ("SELECT password FROM  users WHERE emailAddress = %s")
    csr.execute(query, email)

    for user_actual_password in csr:
        if user_actual_password == password:
            return jsonify(
                success = True,
                authToken = token,
                timeoutTimestamp = token_timeout
            )
        else:
            return jsonify(
                success = False
            )
    return jsonify(
        valid=False
    )


def verify_token(token):
    csr = db.curser()
    query = ("SELECT email, tokenTimeout FROM  users WHERE token = %s")
    csr.execute(query, token)

    for email, token_timeout in csr:
        timestamp = long(token_timeout)
        d = datetime.utcnow()
        unixtime = calendar.timegm(d.utctimetuple())
        if timestamp < unixtime:
            return None
        else:
            return email

    return None