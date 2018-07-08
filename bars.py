import json
from math import sqrt
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        try:
            decoded = json.load(json_file)
        except json.JSONDecodeError:
            return None
    return decoded


def get_biggest_bar(bars_list):
    top_biggest_bar = max(
        bars,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"]
    )
    return top_biggest_bar


def get_smallest_bar(bars_list):
    top_smallest_bar = min(
        bars,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"]
    )
    return top_smallest_bar


def get_closest_bar(bars_list, longitude, latitude):
    top_closest_bar = min(
        bars,
        key=lambda x: (
            x["geometry"]["coordinates"][0] - longitude)**2
        + x["geometry"]["coordinates"][1] - latitude**2

    )
    return top_closest_bar


def print_bar(message, bar):
    print("{0} '{1}'".format(
        message,
        bar["properties"]["Attributes"]["Name"]
    ))


def create_parser():
    parser = argparse.ArgumentParser(
        description="This script prints biggest, smallest and closest bar's name.")
    parser.add_argument(
        "filepath",
        metavar="f",
        type=str,
        help="path to json file"
    )

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = create_parser()
    
    try:
        bars_list = load_data(args.filepath)
        if bars_list is None:
            exit("Error: Invalid json in file {0}.".format(args.filepath))
    except FileNotFoundError as e:
        print("Error: File not found '{0}'".format(e.filename))

    bars = bars_list["features"]
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)
    print_bar("Biggest bar is", biggest_bar)
    print_bar("Smallest bar is", smallest_bar)

    try:
        latitude = float(input("Input latitude of your position: "))
        longitude = float(input("Input longitude of your position: "))
        closest_bar = get_closest_bar(bars_list, longitude, latitude)
        print_bar("Closest bar is", closest_bar)
    except ValueError:
        exit("Enter float numbers - latitude and longitude of your position.")
