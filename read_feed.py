import os
from Adafruit_IO import Client

ADAFRUIT_IO_USERNAME = "tokylabs"
ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def get_latest_value(feed_key):
    try:
        data = aio.receive(feed_key)
        return float(data.value), data.created_at
    except Exception as e:
        print("Error:", e)
        return None, None
