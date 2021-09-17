#!/usr/bin/with-contenv bashio

TIMEZONE=America/Chicago
export TIMEZONE

echo "The current time is `date`"

cd /home/weewx/public_html
python3 -m http.server 8099 &

cd /home/weewx
/home/weewx/bin/weewxd
