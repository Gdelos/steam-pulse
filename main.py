import time

from parser import get_item_data, ITEMS
from alerts import send_alert
from database import save_item, get_average_volume

print("Steam Pulse LIVE...")

while True:

    try:

        for item_name in ITEMS:

            print(f"Checking {item_name}")

            item = get_item_data(item_name)

            print(item)

            volume = item["volume"]
            price = item["price"]

            if not volume:
                continue

            volume_int = int(volume.replace(",", ""))

            save_item(item_name, price, volume_int)

            average_volume = get_average_volume(item_name)

            print("Average volume:", average_volume)

            if average_volume > 0:

                if volume_int > average_volume * 2:

                    text = f"""
🚨 Steam Pulse Alert

Item: {item_name}

Price: {price}
Volume: {volume}

Average Volume: {average_volume}

Unusual volume anomaly detected.
"""

                    print(text)

                    send_alert(text)

            time.sleep(3)

    except Exception as e:

        print("ERROR:", e)

    time.sleep(30)