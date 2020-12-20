import re
from typing import Pattern

MAC_ADDRESS_PATTERN: Pattern = re.compile(r'(?:[a-fA-F0-9]{2}-){5}[a-fA-F0-9]{2}|(?:[a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}|(?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}')
IP_ADDRESS_PATTERN: Pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
