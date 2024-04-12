sudo wget https://github.com/mjadiahmed/flow/blob/main/flows.json -O /home/pi/OpenScan/settings/.node-red/flows.json

sudo pip3 install boto3 rpi_ws281x adafruit-circuitpython-neopixel adafruit-blinka


TO DO:
- Files listing: improve name/date



# Setting Up Node-RED and Flask Services on Raspberry Pi

This guide outlines how to set up Node-RED and Flask services using `systemd` on a Raspberry Pi, as well as installing the `gphoto2` Python module.

## Node-RED Service Setup

### Create the systemd service file for Node-RED

1. Create a new systemd service file for Node-RED:

    ```bash
    sudo nano /etc/systemd/system/nodered.service
    ```

2. Add the following content to the file:

    ```ini
    [Unit]
    Description=Node-RED

    [Service]
    ExecStart=/usr/bin/env node-red
    Restart=always
    RestartSec=10
    User=pi
    Environment=NODE_ENV=production

    [Install]
    WantedBy=multi-user.target
    ```

3. Save the file and exit the text editor.

### Reload systemd configuration

Reload the systemd configuration to apply the changes:

```bash
sudo systemctl daemon-reload

sudo systemctl daemon-reload
sudo nano /etc/systemd/system/flask.service
