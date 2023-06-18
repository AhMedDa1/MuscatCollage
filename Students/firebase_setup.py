# from django.shortcuts import render
# import firebase_admin
# from firebase_admin import firestore

# def my_view(request):
#     # Get a Firestore client
#     db = firestore.client()

#     # Reference to a Firestore collection
#     collection_ref = db.collection('bewell-c09ff')

#     # Query the collection
#     docs = collection_ref.get()

#     # Process the retrieved documents
#     data = []
#     for doc in docs:
#         data.append(doc.to_dict())

#     return render(request, 'bewell.html', {'data': data})
