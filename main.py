import time

from parser import get_item_data, ITEMS
from alerts import send_alert

print("Steam Pulse LIVE...")

last_volumes = {}

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

            old_volume = last_volumes.get(item_name)

            if old_volume:

                if volume_int > old_volume * 2:

                    text = f"""
🚨 Steam Pulse Alert

Item: {item_name}

Price: {price}
Volume: {volume}

Unusual volume spike detected.
"""

                    print(text)

                    send_alert(text)

            last_volumes[item_name] = volume_int

            time.sleep(3)

    except Exception as e:
        print("ERROR:", e)

    time.sleep(30)