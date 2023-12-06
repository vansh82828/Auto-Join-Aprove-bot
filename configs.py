# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "15657755"))
    API_HASH = getenv("API_HASH", "7cce51d4664d010b90ad690e0d5121ad")
    BOT_TOKEN = getenv("BOT_TOKEN", "6678430839:AAELqD5bQMwG9M_wXoQMv-Le4G_VBq8-lSM")
    FSUB = getenv("FSUB", "TagaruPalya_kannad_movie_12")
    CHID = int(getenv("CHID", "-1001526945133"))
    SUDO = list(map(int, getenv("SUDO", "5003133371").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
