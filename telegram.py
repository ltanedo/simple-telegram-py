import requests
import datetime as dt
from pytz import timezone

'''
NOTES
    - If you don't use a Telegram Group (and use a single chat)
      the bot will lose its access after 4 hrs (from the original user's text)

STEPS TO SETUP PYTHON PACKAGES
    pip install requests 
    pip install pytz

STEP TO GET TOKEN HERE
    1. Check BotFather in Telegram APP
        - May need to ask for token again

STEPS TO GET CHAT ID 
    1. Create group in Telegram App
    2. Add bot to group in Telegram App
    3. Make Bot Admin in Telegram App
    4. Check json in -> https://api.telegram.org/bot<YOUR_BOT_TOKEN_HERE_REMOVE_ARROWS>/getUpdates
        - result, my_chat_member, chat, id
'''

def send_telegram(token, chat_id, text, TIMESTAMP_ENABLED=True):

    if TIMESTAMP_ENABLED: 
        stamp = dt.datetime.now(timezone('EST')).strftime("%b %d") #%I:%M%p
        text  = f"({stamp}) {text}"

    resp = requests.get(
        url= 'https://api.telegram.org/bot' + str(token) \
            + '/sendMessage?chat_id=' + str(chat_id) \
            + '&parse_mode=Markdown&text=' + str(text)
    )

    return resp.status_code
