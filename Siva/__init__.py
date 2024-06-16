import os
from pyrogram import Client




# env 
API_ID = os.getenv(API_ID)
API_HASH = os.getenv(API_HASH)
TOKEN = os.getenv(TOKEN)

# client 

Siva = Client(
    name = "Siva",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN,
    plugins = dict(root="Siva")
)
  
  
