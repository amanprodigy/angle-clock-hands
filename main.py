from typing import Tuple
import concurrent.futures
from datetime import datetime
import pytz
from fuzzywuzzy import fuzz

from src.hour_minute import angle_between_minute_hour_hands as angle


def get_time_and_angle(given_time: datetime, time_zone: str) -> Tuple[str, str]:
    """
    Returns tuple of time_in_hh:mm and current_angle b/w minute and hour hands
    for the given time and timezone
    """
    local_timezone = pytz.timezone(time_zone)
    current_local_time = given_time.astimezone(local_timezone)
    current_local_time_string_hh_mm = current_local_time.strftime("%H:%M")
    current_angle = angle(current_local_time_string_hh_mm)
    return (current_local_time_string_hh_mm, current_angle)


def print_time_and_angle(time_zone: str, time_and_angle: Tuple[str, str]) -> None:
    """
    Prints the current time, timezone and the angle
    """
    hh_mm, current_angle = time_and_angle
    print("    ")
    print(f"***** {time_zone} ****")
    print(f"Local time: {hh_mm}. Angle: {current_angle}")
    print("    ")


def run_demo_with_multithread(city_name):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for time_zone in pytz.all_timezones_set:
            if fuzz.partial_ratio(city_name.lower(), time_zone.lower()) > 70:
                current_time = datetime.now()
                future = executor.submit(get_time_and_angle, current_time, time_zone)
                print_time_and_angle(time_zone, future.result())


if __name__ == "__main__":
    your_fav_city_name = str(input("Tell me your favorite city name: "))
    run_demo_with_multithread(your_fav_city_name)
