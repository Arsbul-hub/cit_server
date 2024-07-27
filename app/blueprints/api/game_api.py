import jwt
from flask import jsonify, request
from datetime import datetime
from app import game_api_routes, jwt_tools, game_process, db
from app.models import AccountData, Account


@game_api_routes.route("/edit_account_data", methods=["POST"])
def add_account_data():
    token = request.json["token"]
    username = request.json["username"]
    status, data = jwt_tools.check_auth_token(username, token)
    if data is not None:
        data = data["data"]
        username = data["username"]
        user = db.session.query(Account).filter_by(username=username).first()
        if user is None:
            return {"status": "ERROR", "message": "User not found"}
        account_data = db.session.query(AccountData).filter_by(account_id=user.id).first()
        fio = request.json["fio"]
        phone_number = request.json["phone_number"]
        if not phone_number.isnumeric():
            return {"status": "ERROR", "message": "Phone number is invalid"}
        date_year = request.json["date_year"]
        date_month = request.json["date_month"]
        date_day = request.json["date_day"]
        account_data.fio = fio
        account_data.phone = phone_number
        account_data.date = datetime(year=date_year, month=date_month, day=date_day).isoformat()
        db.session.commit()
        return {"status": "OK", "message": "Signature expired"}
    elif status == "Signature expired. Please":
        return {"status": "ERROR", "message": "Signature expired"}


@game_api_routes.route("/get_account_data", methods=["GET"])
def get_account_data():
    token = request.args["token"]
    username = request.args["username"]
    status, data = jwt_tools.check_auth_token(username, token)
    if data is not None:
        data = data["data"]
        username = data["username"]
        user = db.session.query(Account).filter_by(username=username).first()
        account_data = db.session.query(AccountData).filter_by(account_id=user.id).first()
        if user is None:
            return {"status": "ERROR", "message": "User not found"}

        return {"status": "OK", "data": account_data.to_dict()}
    elif status == "Signature expired. Please":
        return {"status": "ERROR", "message": "Signature expired"}
