import requests
from urllib.parse import quote

headers = {
    "User-Agent": "Mozilla/5.0"
}

ITEMS = ITEMS = [

    "AK-47 | Redline (Field-Tested)",
    "AK-47 | Vulcan (Field-Tested)",
    "AK-47 | Fire Serpent (Field-Tested)",

    "AWP | Asiimov (Battle-Scarred)",
    "AWP | Dragon Lore (Factory New)",
    "AWP | Hyper Beast (Field-Tested)",

    "M4A4 | Howl (Factory New)",
    "M4A1-S | Printstream (Field-Tested)",

    "Desert Eagle | Blaze (Factory New)",
    "USP-S | Kill Confirmed (Field-Tested)",

    "★ Karambit | Doppler (Factory New)",
    "★ Butterfly Knife | Fade (Factory New)",

    "Operation Breakout Weapon Case",
    "CS20 Case",
    "Gamma Case",
    "Gamma 2 Case",
    "Prisma Case",
    "Prisma 2 Case",
    "Danger Zone Case",
    "Recoil Case",
    "Snakebite Case",

    "Sticker Capsule 2",
    "Sticker Capsule",

    "DreamHack 2014 Legends (Holo-Foil)",
    "EMS Katowice 2014 Legends"
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