import pyowm
import time

owm = pyowm.OWM('b88ffe46c83ddb1f183f6f5e661c5b90')

def main():
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
