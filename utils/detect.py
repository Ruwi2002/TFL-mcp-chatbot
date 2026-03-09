from config.stations import stations

tube_lines = [
    "bakerloo",
    "central",
    "circle",
    "district",
    "hammersmith",
    "jubilee",
    "metropolitan",
    "northern",
    "piccadilly",
    "victoria",
    "waterloo",
]


def detect_line(text):

    for line in tube_lines:
        if line in text:
            return line

    return None


def detect_station(text):

    for station in stations:
        if station in text:
            return station

    return None
