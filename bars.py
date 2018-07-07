import json
from math import sqrt


def load_data(filepath):
    with open(filepath) as json_file:
        bars_list = json.load(json_file)
    return bars_list


def get_biggest_bar(bars_list):
    features = bars_list["features"]
    top_biggest_bar = max(
        features,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"]
    )
    return top_biggest_bar


def get_smallest_bar(bars_list):
    features = bars_list["features"]
    top_smallest_bar = min(
        features,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"]
    )
    return top_smallest_bar


def get_closest_bar(bars_list, longitude, latitude):
    features = bars_list["features"]
    top_closest_bar = min(
        features,
        key=lambda x: (
            x["geometry"]["coordinates"][0] - longitude)**2
        + x["geometry"]["coordinates"][1] - latitude**2
    )
    return top_closest_bar

def print_bar(message, bar):
    print("{0} \"{1}\"".format(
        message,
        bar["properties"]["Attributes"]["Name"]
    ))


if __name__ == '__main__':
    bars_list = load_data('bars.json')
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    latitude = float(input("Input latitude:"))
    longitude = float(input("Input longitude:"))

    closest_bar = get_closest_bar(bars_list, longitude, latitude)

    print_bar("Biggest bar is", biggest_bar)
    print_bar("Smallest bar is", smallest_bar)
    print_bar("Closest bar is", closest_bar)
