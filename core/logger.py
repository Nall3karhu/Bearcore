import logging
import os

# Luodaan lokikansio, jos sitä ei ole
os.makedirs("data/logs", exist_ok=True)

# Määritetään lokituksen asetukset
logging.basicConfig(
    filename="data/logs/bearcore.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Luodaan logger-olio
logger = logging.getLogger("BearCore")