from secrets import key
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
import argparse
import pickle #to test smth
from forecastiopy import *
from geopy.geocoders import Nominatim

geolocator = Nominatim()

parser = argparse.ArgumentParser(description="Small weather script.")
parser.add_argument('location', type=str, help="for which to find the weather for")
parser.add_argument('-t', action="store_true", help="print temperature")
parser.add_argument('-s', action="store_true", help="print summary")
parser.add_argument('-o', action="store_true", help="print hourly summary")
parser.add_argument('-d', action="store_true", help="print daily summary")

args = parser.parse_args()

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': '/tmp/weatherpycache/data',
    'cache.lock_dir': '/tmp/weatherpycache/lock'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

@cache.cache("forecast", expire=600)
def get_forecast(locstr):
    location = geolocator.geocode(locstr)
    return ForecastIO.ForecastIO(key, latitude=location.latitude, longitude=location.longitude, units="si")

fo = get_forecast(args.location)
if(args.t):
    print("{: .0f}".format(fo.currently["temperature"]))
if(args.s):
    print(fo.currently["summary"])
if(args.o):
    print(fo.hourly["summary"])
if(args.d):
    print(fo.daily["summary"])
