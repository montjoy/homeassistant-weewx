#!/usr/bin/with-contenv bashio

TIMEZONE=America/Chicago
export TIMEZONE

echo "The current time is `date`"

cd /home/weewx/public_html
echo "Starting the python web server..."
python3 -m http.server 8099 &

cd /home/weewx
echo "Starting weewxd..."
/home/weewx/bin/weewxd
