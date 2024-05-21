from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Flask app
app = Flask(__name__)

# Path to your service account key JSON file
cred = credentials.Certificate('/Users/harinduadhikari/Documents/pythin_firebase/itemmy-firebase-adminsdk-lkzr9-9b824cfecd.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def index():
    # Fetch items from Firestore
    items_ref = db.collection('items')
    docs = items_ref.stream()

    items = []
    for doc in docs:
        items.append(doc.to_dict())

    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
