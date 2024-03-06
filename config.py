from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/5be4505a80556f0652b13.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/203f9e617d4bbe0627b97.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ZeNaKuCHaT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZeNaKuTeCH")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1318826936").split()))


FAILED = "https://te.legra.ph/file/398dceb7be661343981dc.jpg"
