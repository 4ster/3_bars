# TODO: Create tests
# TODO: Refactor code to insure, that each time we use data, it is exist and valid

import json
from math import sqrt

def load_data(filepath):
    """Load json file"""
    with open(filepath) as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    """Return record ID of the biggest bar """
    top_biggest = sorted(data["features"],
                         key=lambda x: x["properties"]["Attributes"]["SeatsCount"], reverse=True)
    return top_biggest[0]["properties"]["RowId"]


def get_smallest_bar(data):
    """Return record ID of the smallest bar. Zero seats count allowed. """
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


def get_bar_name(data, row_id):
    """Return basic information in dict data about bar with RowID equals second parameter(row_id)"""
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
