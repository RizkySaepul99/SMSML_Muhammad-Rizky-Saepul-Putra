import requests
import random
import time

URL = "http://localhost:9000/invocations"
HEADERS = {"Content-Type": "application/json"}

FEATURES = [
    "PAC","SHO","PAS","DRI","DEF","PHY",
    "Acceleration","Sprint Speed","Positioning","Finishing",
    "Shot Power","Long Shots","Volleys","Penalties",
    "Vision","Crossing","Free Kick Accuracy",
    "Short Passing","Long Passing","Curve",
    "Dribbling","Agility","Balance","Reactions",
    "Ball Control","Composure",
    "Interceptions","Heading Accuracy","Def Awareness",
    "Standing Tackle","Sliding Tackle",
    "Jumping","Stamina","Strength","Aggression",
    "Weak foot","Skill moves"
]

def random_player():
    data = []
    for feature in FEATURES:
        if feature in ["Weak foot", "Skill moves"]:
            data.append(random.randint(1, 5))     # khusus skill
        else:
            data.append(random.randint(40, 99))   # atribut pemain
    return data


if __name__ == "__main__":
    while True:
        payload = {
            "dataframe_split": {
                "columns": FEATURES,
                "data": [random_player()]
            }
        }

        response = requests.post(URL, json=payload, headers=HEADERS)

        print("Status:", response.status_code)
        print("Prediction:", response.text)

        time.sleep(3)  # request tiap 3 detik
