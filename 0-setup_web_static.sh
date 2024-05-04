#!/usr/bin/python3

# Install Nginx if it not already installed
apt-get update
apt-get install nginx

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
ufw allow 'Nginx HTTP'

mkdir -P /data/web_static/

mkdir -P /data/web_static/shared/
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -P /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

config_file="/etc/nginx/sites-available/default"

sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' $config_file

service nginx restart

exit 0
