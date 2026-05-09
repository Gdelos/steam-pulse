import requests

URL = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=AK-47%20%7C%20Redline%20(Field-Tested)"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_item_data():

    print("Sending request...")

    response = requests.get(
        URL,
        headers=headers,
        proxies={},
        timeout=10
    )

    print("Response received")

    data = response.json()

    return {
        "price": data.get("lowest_price"),
        "volume": data.get("volume")
    }