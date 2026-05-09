import time

from parser import get_item_data, ITEMS
from alerts import send_alert
from database import (
    save_item,
    get_average_volume,
    get_record_count
)

print("Steam Pulse LIVE...")

last_alerts = {}

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

            record_count = get_record_count(item_name)

            print("Records:", record_count)

            if record_count < 5:

                print("Not enough data yet")

                time.sleep(2)

                continue

            average_volume = get_average_volume(item_name)

            print("Average volume:", average_volume)

            if average_volume > 0:

                anomaly_score = round(volume_int / average_volume, 2)

                print("Anomaly score:", anomaly_score)

                current_time = time.time()

                last_alert_time = last_alerts.get(item_name, 0)

                if anomaly_score > 2 and current_time - last_alert_time > 3600:

                    text = f"""
🚨 Steam Pulse Anomaly

Item: {item_name}

Price: {price}
Volume: {volume}

Average Volume: {average_volume}
Anomaly Score: {anomaly_score}x

Records: {record_count}
"""

                    print(text)

                    send_alert(text)

                    last_alerts[item_name] = current_time

            time.sleep(3)

    except Exception as e:

        print("ERROR:", e)

    time.sleep(30)