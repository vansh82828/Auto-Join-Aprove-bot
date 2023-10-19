# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29849415"))
    API_HASH = getenv("API_HASH", "0dd6c10897b85d7f10a8dcdeb74f8b8a")
    BOT_TOKEN = getenv("BOT_TOKEN", "6356800097:AAGBRWOaHu8f4h9e424GChabOGmOcQZpi5s")
    FSUB = getenv("FSUB", "VJ_Botz")
    CHID = int(getenv("CHID", "-1001787034706"))
    SUDO = list(map(int, getenv("SUDO", "5165943027").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
