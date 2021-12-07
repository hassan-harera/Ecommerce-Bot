import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from google.cloud import storage

cred = credentials.Certificate('private_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("Products").document()
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

client = storage.Client(credentials=cred)
bucket = client.get_bucket("products")
blob = bucket.blob("123.png")
blob.upload_from_string('this is test content!')


fStorage = storage.Client().current_batch
print(fStorage)