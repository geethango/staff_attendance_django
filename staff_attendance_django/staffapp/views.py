# views.py

from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, firestore

#from django.template import loader
def home(request):
    return render(request, 'home.html')

def firebase_data(request):
    
    # Initialize Firebase Admin SDK
    if not firebase_admin._apps:
      cred = credentials.Certificate(r'C:\Users\geeth\Desktop\project\staff_attendance_django\staff_attendance_django\ServiceAccountKey.json')
      firebase_admin.initialize_app(cred)
      
    
    # Get Firestore client
    db = firestore.client()
    
    # Fetch data from Firebase
    firebase_data = []
    docs = db.collection('collection').get()
    for doc in docs:
        firebase_data.append(doc.to_dict())  # Convert Firebase data to Python dict
    print(firebase_data)
    return render(request,'home.html', {'firebase_data': firebase_data})
