import json
from math import sqrt
import argparse


def load_data(filepath):
    try:
        with open(filepath) as json_file:
            decoded_json = json.load(json_file)
        return decoded_json, None
    except json.JSONDecodeError as error:
        return None, error
    except FileNotFoundError as error:
        return None, error


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


def get_closest_bar(bars_list, latitude, longitude):
    if (longitude is None or latitude is None):
        return None
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
    parser.add_argument(
        "-lat",
        "--latitude",
        type=float,
        help="Latitude",
        default = None
    )
    parser.add_argument(
        "-long",
        "--longitude",
        type=float,
        help="Longitude",
        default = None
    )

    args = parser.parse_args()
    return args


def ask_user_coord(coord_name):
    try:
        coordinate = float(
            input("Input {0} of your position: ".format(coord_name)))
        return coordinate
    except ValueError:
        return None


def search_bars(bars_list, latitude, longitude):
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)
    closest_bar = get_closest_bar(bars_list, latitude, longitude)

    return biggest_bar, smallest_bar, closest_bar


if __name__ == '__main__':
    args = create_parser()
    bars_list, err = load_data(args.filepath)
    
    if err is not None:
        exit("Error in file {0}\n{1}".format(
            args.filepath, err))
    bars = bars_list["features"]
    latitude = args.latitude or ask_user_coord("latitude")
    longitude = args.longitude or ask_user_coord("longitude")
    
    biggest_bar, smallest_bar, closest_bar = search_bars(bars_list, latitude, longitude)
    print_bar("Biggest bar is", biggest_bar)
    print_bar("Smallest bar is", smallest_bar)
    if closest_bar is None:
        exit("Can't print closest bar. Enter float numbers - coordinates of your position.")
    print_bar("Closest bar is", closest_bar)
