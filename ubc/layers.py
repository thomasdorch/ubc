from phidl.utilities import load_lyp
from ubc.config import CONFIG

lys = load_lyp(str(CONFIG["lyp"]))


if __name__ == "__main__":
    print(lys)
