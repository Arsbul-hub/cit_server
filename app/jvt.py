from datetime import datetime, timedelta

import jwt


class Jwt:
    def __init__(self, config):
        self.secret_key = config.JWS_SECRET_KEY

    def generate_auth_token(self, username):
        return jwt.encode({"iss": username, "exp": datetime.now() + timedelta(days=10),
                           "data": {'username': username}}, self.secret_key)

    def check_auth_token(self, username, token):
        decoded = None
        try:
            decoded = jwt.decode(token, self.secret_key, issuer=username, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please", None
        except:
            return "Something", None
        return 200, decoded
