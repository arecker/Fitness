import requests
import json
import click


class APIRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.key = get_admin_key()

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


# Interface
@click.group()
def cli():
    """
    This script tracks workout sessions and weight measurements.
    """
    pass


@cli.group()
def weight():
    """
    weight tracking
    """
    pass


@cli.group()
def session():
    """
    workout session tracking
    """

@weight.command('add')
@click.option('--weight', prompt=True, help="weight measurement in pounds", type=click.FLOAT)
def add_weight(weight):
    """
    adds a weight measurement (timestamped)
    """
    wm = WeightMeasurement(weight=weight)
    try:
        wm.save()
        click.echo('Weight measurement saved')
    except:
        click.echo('Something went wront.  Weight not saved')


@session.command('add')
@click.option('--distance', prompt=True, help="distance ran in miles", type=click.FLOAT)
@click.option('--speed', prompt=True, help="average speed in mph", type=click.FLOAT)
def add_session(distance, speed):
    """
    adds a workout session (timestamped)
    """
    fs = WorkoutSession(distance=distance, speed=speed)
    try:
        fs.save()
        click.echo('Workout session saved')
    except:
        click.echo('Something went wront.  Workout session not saved')


if __name__ == '__main__':
    cli()



