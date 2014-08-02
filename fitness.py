import requests
import json


class APIRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.key = 'boob'#get_admin_key()

    def post(self, path_from_base, data):
        response = requests.post(self.base_url + path_from_base + '?admin=' + self.key, data=data)
        if response.status_code in (500, 404, 403):
            raise Exception("API Failed")


class WorkoutSession:
    def __init__(self, distance, speed):
        self.APIClass = APIRequest('http://api.alexrecker.com/fitness/workoutsession')
        self.distance = distance
        self.speed = speed

    def save(self):
        path = '/add/'
        data = {
            "distance": self.distance,
            "speed": self.speed
        }

        response = self.APIClass.post(path_from_base=path, data=json.dumps(data))


class WeightMeasurement:
    def __init__(self, weight):
        self.APIClass = APIRequest('http://api.alexrecker.com/fitness/weightmeasurement')
        self.weight = weight


    def save(self):
        path = '/add/'
        data = {
            "weight": self.weight
        }

        response = self.APIClass.post(path_from_base=path, data=json.dumps(data))


def get_admin_key():
    with open('.keys.json') as file:
        return json.load(file)["admin"]

