import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY

def generate_token(user_id):
    return jwt.encode({
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=5)
    }, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return None
