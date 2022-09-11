import json
import os

import firebase_admin
from firebase_admin import firestore

def main():
    os.system("export GOOGLE_APPLICATION_CREDENTIALS=/Users/shawnpatel/Documents/Radgard/animal-farm-e321d-3e78152a68ad.json")

    default_app = firebase_admin.initialize_app()

    db = firestore.client()
    plants_ref = db.collection("laraCloudSettings").document("plants")

    with open("plants.json") as file:
        data = json.load(file)
        plants_ref.set(data)

if __name__ == "__main__":
    main()