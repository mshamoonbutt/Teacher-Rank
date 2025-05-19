import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase Admin SDK
cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS", "path_to_firebase_credentials.json"))
firebase_admin.initialize_app(cred)

def verify_firebase_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise Exception(f"Invalid token: {str(e)}") 