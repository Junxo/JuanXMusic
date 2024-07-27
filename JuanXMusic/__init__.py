from JuanXMusic.core.bot import Dil
from JuanXMusic.core.dir import dirr
from JuanXMusic.core.git import git
from JuanXMusic.core.userbot import Userbot
from JuanXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Dil()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
