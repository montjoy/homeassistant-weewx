#!/usr/bin/with-contenv bashio

cd /home/weewx
/home/weewx/bin/weewxd -d

cd /home/weewx/public_html
python3 -m http.server 8088
