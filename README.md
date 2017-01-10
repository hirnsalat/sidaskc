sidaskc - a SImple DArkSKy Client
=================================

The goal for this little command line tool was to be used in system monitors, status bars, command line prompts and similar things. It looks up the location using `geopy`, downloads weather information via `forecastiopy`, and caches the result using `Beaker`. Which information should be output is controlled by command line switches. Unfortunately, startup is a bit slow, I might fix that in some way later.

Obviously, this is [Powered by Dark Sky](https://darksky.net/poweredby/).

Released under the MIT License (see LICENSE).

setup
-----

Just doing

    python setup.py install

should do the trick.
