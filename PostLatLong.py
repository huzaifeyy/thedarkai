from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

file1 = open('postcode1.txt', 'r')
locator = Nominatim(user_agent="myGeocoder")
lines = file1.readlines()

for line in lines:
    try:
        location = locator.geocode(line, timeout=100)
        geocode = RateLimiter(locator.geocode, min_delay_seconds=1, return_value_on_exception=None)
        print(line, ",", location.latitude,",",   location.longitude)
    except (AttributeError):
        print("Error", line)

lines = file1.readlines()








