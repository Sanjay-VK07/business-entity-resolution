import re

STOP_WORDS = r'\b(pvt|ltd|private|limited|m/s)\b'

def normalize_name(name: str) -> str:
    if not isinstance(name, str):
        return ""
    name = name.lower()
    name = re.sub(STOP_WORDS, '', name)
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def normalize_address(addr: str) -> str:
    if not isinstance(addr, str):
        return ""
    addr = addr.lower()
    addr = addr.replace("mg rd", "mahatma gandhi road")
    addr = addr.replace("rd.", "road").replace(" rd ", " road ")
    addr = addr.replace("st.", "street").replace(" st ", " street ")
    addr = addr.replace("no.", "").replace("no ", "")
    addr = re.sub(r'\s+', ' ', addr)
    return addr.strip()