import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# Update data with known key
db.collection('persons').document("p1").update({"age": 50}) # field already exists
db.collection('persons').document("p1").update({"age": firestore.Increment(2)}) # increment a field
db.collection('persons').document("p1").update({"occupation": "engineer"}) # the field will be added
db.collection('persons').document("p1").update({"occupation": "engineer"})
db.collection('persons').document("p2").update({"socials": firestore.ArrayRemove(['linkedin'])})
db.collection('persons').document("p1").update({"socials": firestore.ArrayUnion(['linkedin'])})
