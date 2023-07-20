
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(r"D:\module6-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def insert():

    task = input("Please enter the task name: ")
    status = input('Enter the current status of the task: ')

    data = {
    'task': task,
    'status': status
}

    doc_ref = db.collection('tasksCollection').document()
    doc_ref.set(data)

    print('Document ID: ', doc_ref.id)
    menu()

def modify():
    id = input("Please enter the document ID: ")
    category = input("Please enter category ID: ")
    new_value = input("Please enter new value: ")
    db.collection('tasksCollection').document(id).update({category:new_value})
    menu()

def delete():
    id = input("Please enter the document ID: ")
    db.collections('tasksCollection').document(id).delete()
    menu()

def retrieve():
    doc_id = input('Please enter document ID: ')
    doc_ref = db.collection("tasksCollection").document(doc_id)

    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")
    menu()

def menu():
    print("Please choose an option")
    print('MENU: \n  1. Insert new data \n  2. Modify current data \n  3. Delete data \n  4. Retrieve current data \n  5. End')
    x = input("> ")
    if x == '1':
        insert()
    elif x == '2':
        modify()
    elif x == '3':
        delete()
    elif x == '4':
        retrieve()
    elif x == '5':
        return
    else:
        print("Please choose one of the 4 options listed")
        menu()


menu()







