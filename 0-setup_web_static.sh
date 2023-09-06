#!/usr/bin/env bash
# creates a deployment script for web static

sudo apt-get -y update
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Simple content" | sudo tee /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
    rm -R "/data/web_static/current"
fi

ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '17i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
