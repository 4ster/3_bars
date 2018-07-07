import json
from math import sqrt


def load_data(filepath):
    with open(filepath) as f:
        bars_list = json.load(f)
    return bars_list


def get_biggest_bar(bars_list):
    top_biggest = max(bars_list["features"],
                      key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return top_biggest["properties"]["RowId"]


def get_smallest_bar(bars_list):
    top_smallest = min(bars_list["features"],
                       key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return top_smallest["properties"]["RowId"]


def get_closest_bar(bars_list, longitude, latitude):
    top_closest = min(bars_list["features"],
                      key=lambda x: (x["geometry"]["coordinates"][0] - longitude)**2 + x["geometry"]["coordinates"][1] - latitude**2)
    return top_closest["properties"]["RowId"]


def get_bar_name(bars_list, row_id):
    # Return name of bar with given RowId
    for b in bars_list["features"]:
        if(b["properties"]["RowId"] == row_id):
            return b["properties"]["Attributes"]["Name"]


if __name__ == '__main__':
    bars_list = load_data('bars.json')
    biggest_id = get_biggest_bar(bars_list)
    smallest_id = get_smallest_bar(bars_list)

    latitude = float(input("Input latitude:"))
    longitude = float(input("Input longitude:"))

    closest_id = get_closest_bar(bars_list, longitude, latitude)

    print("Biggest bar is \"{0}\"".format(get_bar_name(bars_list, biggest_id)))
    print("Smallest bar is \"{0}\"".format(
        get_bar_name(bars_list, smallest_id)))
    print("Closest bar is \"{0}\"".format(get_bar_name(bars_list, closest_id)))
