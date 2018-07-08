import json
from math import sqrt
import argparse


def load_data(filepath):
    try:
        with open(filepath) as json_file:
            decoded = json.load(json_file)
        return decoded, None
    except json.JSONDecodeError as e:
        return None, e
    except FileNotFoundError as e:
        return None, e
    


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


def search_bars(bars_list):
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    try:
        latitude = float(input("Input latitude of your position: "))
        longitude = float(input("Input longitude of your position: "))
        closest_bar = get_closest_bar(bars_list, longitude, latitude)
    except ValueError:
        closest_bar = None
    return biggest_bar, smallest_bar, closest_bar


if __name__ == '__main__':
    args = create_parser()
    bars_list, err = load_data(args.filepath)
    if err is not None:
        exit("Error in file {0}\n{1}".format(
            args.filepath, err))
    bars = bars_list["features"]
    biggest_bar, smallest_bar, closest_bar = search_bars(bars_list)
    print_bar("Biggest bar is", biggest_bar)
    print_bar("Smallest bar is", smallest_bar)
    if closest_bar is None:
        exit("Can't print closest bar. Enter float numbers - coordinates of your position.")
    print_bar("Closest bar is", closest_bar)
