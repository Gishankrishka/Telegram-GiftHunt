#Copyright  ©  t.me/gishandev


from pyrogram import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

pbot = Client(
    "gifthunt",
    api_id=123456789,
    api_hash="abcd1234",
    phone_number="+94xxxxxxxx"
)
owner=1884885842 # replace with ur telegram id
max_price=500 
max_available_amount=15000

async def check_star_gifts():
    await pbot.send_message("krishdev", "working")
    while True:
        try:
            gifts = await pbot.get_available_gifts()  # Fetch available gifts
            for gift in gifts:
                if not gift.is_sold_out and gift.price == max_price and gift.is_limited and gift.available_amount <= max_available_amount:
                    await pbot.send_gift(
                        chat_id=owner,
                        gift=gift.id,
                    )
                    print(gift)
                    break 
        except Exception as e:
            print(f"Error fetching or sending gifts: {e}")  

if __name__ == "__main__":
    try:
        pbot.start()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(check_star_gifts())
        idle()
    except Exception as e:
        print(str(e))

