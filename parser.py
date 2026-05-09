import requests
from urllib.parse import quote

headers = {
    "User-Agent": "Mozilla/5.0"
}

ITEMS = [

    # AK-47
    "AK-47 | Redline (Field-Tested)",
    "AK-47 | Vulcan (Field-Tested)",
    "AK-47 | Fire Serpent (Field-Tested)",
    "AK-47 | Neon Rider (Field-Tested)",
    "AK-47 | Bloodsport (Field-Tested)",

    # AWP
    "AWP | Asiimov (Battle-Scarred)",
    "AWP | Dragon Lore (Factory New)",
    "AWP | Hyper Beast (Field-Tested)",
    "AWP | Containment Breach (Field-Tested)",
    "AWP | Wildfire (Field-Tested)",

    # M4
    "M4A4 | Howl (Factory New)",
    "M4A1-S | Printstream (Field-Tested)",
    "M4A4 | Asiimov (Field-Tested)",
    "M4A1-S | Hyper Beast (Field-Tested)",

    # Pistols
    "Desert Eagle | Blaze (Factory New)",
    "USP-S | Kill Confirmed (Field-Tested)",
    "USP-S | Printstream (Field-Tested)",
    "Glock-18 | Fade (Factory New)",

    # Knives
    "★ Karambit | Doppler (Factory New)",
    "★ Butterfly Knife | Fade (Factory New)",
    "★ M9 Bayonet | Doppler (Factory New)",
    "★ Skeleton Knife | Fade (Factory New)",

    # Gloves
    "★ Sport Gloves | Pandora's Box (Field-Tested)",
    "★ Specialist Gloves | Fade (Field-Tested)",

    # Cases
    "Operation Breakout Weapon Case",
    "CS20 Case",
    "Gamma Case",
    "Gamma 2 Case",
    "Prisma Case",
    "Prisma 2 Case",
    "Danger Zone Case",
    "Recoil Case",
    "Snakebite Case",
    "Fracture Case",
    "Clutch Case",
    "Glove Case",
    "Spectrum Case",
    "Spectrum 2 Case",
    "Revolution Case",
    "Kilowatt Case",

    # Capsules
    "Sticker Capsule",
    "Sticker Capsule 2",
    "Community Sticker Capsule 1",
    "Community Sticker Capsule 2",

    # Tournament Capsules
    "DreamHack 2014 Legends (Holo-Foil)",
    "EMS Katowice 2014 Legends",
    "Stockholm 2021 Legends Sticker Capsule",
    "Antwerp 2022 Legends Sticker Capsule",

    # Agents
    "Sir Bloody Darryl Royale | The Professionals",
    "Number K | The Professionals",

    # Collectibles
    "Music Kit | Scarlxrd, CHAIN$AW.LXADXUT.",
    "StatTrak™ Music Kit | The Verkkars, EZ4ENCE"
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