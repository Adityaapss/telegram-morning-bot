from telegram import Bot
from datetime import datetime
import asyncio
import schedule
import time

# === CONFIGURATION ===
BOT_TOKEN = "8389179359:AAHmL0oG92ouBsBbjfP4hvrJeHtjW3TeQnQ"
CHAT_ID = "-1002529390945"

bot = Bot(token=BOT_TOKEN)

# === MESSAGE CONTENT ===
MESSAGE = """*🌞 Good Morning Traders! ☀️*

A new day, a new chart, a new opportunity! 📈  
Stay focused, follow your plan, and remember —  
*Patience + Discipline = Profits 💰*

Let’s make smart moves today.  

🤝 *Trade Together, Grow Together!*  
                    *TEAM BJH*

📲 *Stay Connected:*  
👉 [Instagram](https://www.instagram.com/teambjh/)  
👉 [YouTube](https://www.youtube.com/@TeamBJH)

*❤️ Don’t forget to Like, Follow, and Subscribe!*  
"""

# === FUNCTION TO SEND MESSAGE ===
async def send_message():
    await bot.send_message(
        chat_id=CHAT_ID,
        text=MESSAGE,
        parse_mode="Markdown"
    )
    print(f"✅ Message sent at {datetime.now()}")

def job():
    asyncio.run(send_message())

# Send immediately (for testing)
asyncio.run(send_message())

# Schedule message every day at 8:00 AM
schedule.every().day.at("08:00").do(job)

print("Bot is running... waiting for 8:00 AM ⏰")

while True:
    schedule.run_pending()
    time.sleep(30)
