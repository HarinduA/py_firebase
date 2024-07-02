from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Flask app
app = Flask(__name__)

# Path to your service account key JSON file

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
