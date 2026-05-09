import time

from parser import get_item_data
from alerts import send_alert

print("Steam Pulse started...")

last_volume = None

while True:

    try:

        print("Checking Steam...")

        item = get_item_data()

        print("DATA:", item)

        volume = item["volume"]
        price = item["price"]

        if True:

            text = f"""
🚨 Steam Pulse Alert

Item: AK-47 | Redline
Price: {price}
Volume: {volume}

Volume changed.
"""

            print(text)

            send_alert(text)

        last_volume = volume

    except Exception as e:
        print("ERROR:", e)

    time.sleep(30)