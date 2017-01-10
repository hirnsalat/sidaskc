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

Your DarkSky API key (get one for free [here](https://darksky.net/dev/)) needs to be exported for this to work, so add something like this:

    export DARK_SKY_API=0123456789abcdef0123456789abcdef

to your `.bashrc`.

If you want don't want to install it system wide, you can use a virtual environment, for example:

    virtualenv venv
    source venv/bin/activate
    python setup.py install

This would put the executable under `venv/bin/sidaskc`, and you can link it, write a wrapper script or call it directly.
