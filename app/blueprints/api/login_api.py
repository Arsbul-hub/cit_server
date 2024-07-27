from flask import jsonify, request
from app import login_api_routes, jwt_tools, db, game_process
from app.models import Account, AccountData


@login_api_routes.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    account = db.session.query(Account).filter_by(username=username).first()
    if not account:
        return jsonify({"status": "error", "code": 404, "message": "Аккаунт с таким именем не был найден"})
    if not account.check_password(password):
        return jsonify({"status": "error", "code": 400, "message": "Неверный пароль"})

    return jsonify({"status": "success",
                    "token": jwt_tools.generate_auth_token(account.username)
                    })


@login_api_routes.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]

    account = db.session.query(Account).filter_by(username=username).first()
    if account is not None:
        return jsonify({"status": "error", "code": 405, "message": "Account with this username already exists"})
    new_account = Account()
    new_account.username = username
    new_account.set_password(password)


    db.session.add(new_account)
    db.session.commit()
    account_data = AccountData()
    account_data.account_id = new_account.id
    db.session.add(account_data)
    db.session.commit()
    return jsonify({
        "status": "success",
        "token": jwt_tools.generate_auth_token(username)
    })
