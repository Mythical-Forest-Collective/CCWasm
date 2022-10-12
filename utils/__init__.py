import re

_ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

escape_ansi = lambda text: _ansi_escape('', text)