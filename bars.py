# TODO: Create tests
# TODO: Refactor code to insure, that each time we use data, it is exist

import json
from math import sqrt

# Loads json file


def load_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    """Return record ID of the biggest bar """
    top_biggest = sorted(data["features"],
                         key=lambda x: x["properties"]["Attributes"]["SeatsCount"], reverse=True)
    return top_biggest[0]["properties"]["RowId"]


def get_smallest_bar(data):
    """Return record ID of the smallest bar """
    top_smallest = sorted(data["features"],
                          key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return top_smallest[0]["properties"]["RowId"]


def get_closest_bar(data, longitude, latitude):
    """Return the record ID of the closest bar. Supposing Earth surface is flat. 
    Measure units are ignored. Comparing only square distances.
    """
    top_closest = sorted(data["features"],
                         key=lambda x: (x["geometry"]["coordinates"][0] - longitude)**2 + x["geometry"]["coordinates"][1] - latitude**2)
    return top_closest[0]["properties"]["RowId"]


def get_info(data, row_id):
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

    print("Biggest bar is \"{0}\"".format(get_info(data, biggest_id)))
    print("Smallest bar is \"{0}\"".format(get_info(data, smallest_id)))
    print("Closest bar is \"{0}\"".format(get_info(data, closest_id)))
