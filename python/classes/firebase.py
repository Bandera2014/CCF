#https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
from time import time
from firebase_admin import initialize_app, credentials, db
import sys

class FirebaseClass:
    def __init__(self):
        try:
            self.default_app = initialize_app(credentials.Certificate('./private/private.json'),{'databaseURL': "https://sictc-career-fair-default-rtdb.firebaseio.com/"})
        except:
            self.default_app = initialize_app(credentials.Certificate(f"{sys._MEIPASS}/private.json"),{'databaseURL': "https://sictc-career-fair-default-rtdb.firebaseio.com/"})
    
    #https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
    def new(self,dict):
        ref = db.reference(f"/Items/{int(time()*1000)}")
        for i in dict.keys():
            ref.child(i).set(dict[i])
    
    def getItems():
        tempdata = db.reference(f"/Items").get(True)
        data = []
        for i in tempdata[0]:
            data.append(str(tempdata[0][i]["name"]))
        return data
    
    def delItemFromIndex(index):
        tempdata = db.reference(f"/Items").get(True)
        db.reference(f"/Items/{list(tempdata[0].keys())[index]}").delete()