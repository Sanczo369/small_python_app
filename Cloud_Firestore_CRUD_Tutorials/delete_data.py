import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


# Delete a document - known ID
db.collection('persons').document("p1").delete()

# Delete a field - known ID
db.collection('persons').document("p2").update("age", firestore.DELETE_FIELD)
