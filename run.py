import socket
import pyowm
import time
import sys
import webcolors
import numpy as np

owm = pyowm.OWM('b88ffe46c83ddb1f183f6f5e661c5b90')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9999)

colors = ['F0F8FF', 'FAEBD7', '00FFFF', 'A52A2', 'deb887']


def main():
    sock.connect(server_address)
    # Setup
    sock.sendall(b'setup -n 12\n')
    time.sleep(1)
    sock.sendall(b'init\n')
    i = 0
    while True:
      time.sleep(1)
      message = "fill -c 0\n"
      sock.sendall(bytes(message, 'utf-8'))
      idx=np.random.randint(4)
      i = (i+1)%12
      message = "write -i " + str(i) + " -c " + colors[idx] + "\n"
      sock.sendall(bytes(message, 'utf-8'))
    while True:
        # Search for weather in London
        observation = owm.weather_at_place('London, GB')
        w = observation.get_weather()
        print(w)

        # Weather details
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        time.sleep(60)


if __name__ == "__main__":
    # execute only if run as script
    main()
