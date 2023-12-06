# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "2238786"))
    API_HASH = getenv("API_HASH", "e449d6cc630583d0b415b286eedb9192")
    BOT_TOKEN = getenv("BOT_TOKEN", "6900717691:AAHTC2hKMhNjEJqEKUIbsE-VkdnGB6a5dMA")
    FSUB = getenv("FSUB", "PS_BOTz")
    CHID = int(getenv("CHID", "-1001910352559"))
    SUDO = list(map(int, getenv("SUDO", "950958796").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Auto: Auto@cluster0.xnmdjg4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
