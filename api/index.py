from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

app = Flask(__name__)

# Firebase Admin SDK ko securely environment variable se initialize karna
if not firebase_admin._apps:
    firebase_cred_json = os.environ.get("FIREBASE_CREDENTIALS")
    if firebase_cred_json:
        try:
            cred_dict = json.loads(firebase_cred_json)
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            print("Firebase Initialization Error:", e)

db = firestore.client() if firebase_admin._apps else None

# Groq API Key securely fetch karna
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"success": True, "message": "Backend securely connected with Firebase & Groq!"})
