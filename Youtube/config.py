import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7714597593:AAHvy7XFZo_p1kXmQStUBFKqi3gWI20hfkc")
    API_ID = int(os.environ.get("API_ID", "29882586" ))
    API_HASH = os.environ.get("API_HASH", "a1fb8af0655e315111cd43177bac52dc")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002067831129")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
