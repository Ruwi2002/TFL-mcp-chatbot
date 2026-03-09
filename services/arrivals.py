import requests
from config.stations import stations


def get_next_train(station_name):

    stop_id = stations[station_name]

    url = f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals"

    try:
        response = requests.get(url)
        data = response.json()

        if not data:
            return "No train arrival data available."

        data.sort(key=lambda x: x["timeToStation"])

        train = data[0]

        minutes = int(train["timeToStation"] / 60)
        line = train["lineName"]
        destination = train["destinationName"]

        return f"Next {line} train to {destination} arrives in {minutes} minutes."

    except:
        return "Could not retrieve train arrival information."
