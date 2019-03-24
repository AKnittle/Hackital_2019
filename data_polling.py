"""Python Module used for """
import googlemaps
import gmplot
from datetime import datetime


api_file = open("api_key.txt", "r")
api_key = api_file.read()


def poll_data():
    gmap = googlemaps.Client(key=api_key)
    # geocode_result = gmap.geocode("First St SE, Washington, DC 20004")
    # print(geocode_result)
    now = datetime.now()
    directions_result_raw = gmap.directions("Washington Monument",
                                        "Lincoln Memorial",
                                        mode="transit",
                                        departure_time=now)
    print(directions_result_raw)
    return


def main():
    poll_data()
    return


if __name__ == "__main__":
    main()
