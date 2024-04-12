sudo wget https://github.com/mjadiahmed/flow/blob/main/flows.json -O /home/pi/OpenScan/settings/.node-red/flows.json

sudo pip3 install boto3 rpi_ws281x adafruit-circuitpython-neopixel adafruit-blinka


TO DO:
- Files listing: improve name/date



# auto startup Node-Red
sudo nano /etc/systemd/system/nodered.service

[Unit]
Description=Node-RED

[Service]
ExecStart=node-red
Restart=always
RestartSec=10
User=root
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target

sudo systemctl enable nodered.service
sudo systemctl daemon-reload
sudo nano /etc/systemd/system/flask.service
