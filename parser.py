import requests
from urllib.parse import quote

headers = {
    "User-Agent": "Mozilla/5.0"
}

ITEMS = [
    "AK-47 | Redline (Field-Tested)",
    "AWP | Asiimov (Battle-Scarred)",
    "M4A4 | Howl (Factory New)",
    "Desert Eagle | Blaze (Factory New)",
    "USP-S | Kill Confirmed (Field-Tested)"
]

def get_item_data(item_name):

    encoded_name = quote(item_name)

    url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={encoded_name}"

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    data = response.json()

    return {
        "name": item_name,
        "price": data.get("lowest_price"),
        "volume": data.get("volume")
    }