import json
from math import sqrt


def load_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    top_biggest = max(data["features"],
                         key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return top_biggest["properties"]["RowId"]


def get_smallest_bar(data):
    top_smallest = min(data["features"],
                          key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return top_smallest["properties"]["RowId"]


def get_closest_bar(data, longitude, latitude):
    top_closest = min(data["features"],
                         key=lambda x: (x["geometry"]["coordinates"][0] - longitude)**2 + x["geometry"]["coordinates"][1] - latitude**2)
    return top_closest["properties"]["RowId"]


def get_bar_name(data, row_id):
    # Return name of bar with given RowId
    for b in data["features"]:
        if(b["properties"]["RowId"] == row_id):
            return b["properties"]["Attributes"]["Name"]


if __name__ == '__main__':
    data = load_data('bars.json')
    biggest_id = get_biggest_bar(data)
    smallest_id = get_smallest_bar(data)

    latitude = float(input("Input latitude:"))
    longitude = float(input("Input longitude:"))

    closest_id = get_closest_bar(data, longitude, latitude)

    print("Biggest bar is \"{0}\"".format(get_bar_name(data, biggest_id)))
    print("Smallest bar is \"{0}\"".format(get_bar_name(data, smallest_id)))
    print("Closest bar is \"{0}\"".format(get_bar_name(data, closest_id)))
