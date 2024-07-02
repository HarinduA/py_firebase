import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Path to your service account key JSON file

firebase_admin.initialize_app(cred)

db = firestore.client()

items = [
    {"itemCode": "951015", "description": "TOP CRUST BREAD 450G", "qty": 1, "price": 149.00, "amount": 149.00},
    {"itemCode": "951009", "description": "KEELLS SANDWICH BREAD 450G", "qty": 1, "price": 280.00, "amount": 280.00},
    {"itemCode": "111451", "description": "SAMS CHICKEN SAUSAGE 200G", "qty": 1, "price": 590.00, "amount": 590.00},
    {"itemCode": "118833", "description": "KEELLS ONION SNACKS 50G", "qty": 1, "price": 179.00, "amount": 179.00},
    {"itemCode": "122081", "description": "AYUSH ANTI CAVITY TOOTHPASTE 110G", "qty": 2, "price": 285.00, "amount": 570.00},
    {"itemCode": "6255", "description": "NESTOMALT ACTIGEN PKT 175G", "qty": 1, "price": 390.00, "amount": 390.00},
    {"itemCode": "115575", "description": "AMBEWELA CHEESE SPREAD 100G", "qty": 1, "price": 370.00, "amount": 370.00}
]

# Add items to Firestore
for item in items:
    db.collection('items').add(item)

print("Items added to Firestore successfully.")
