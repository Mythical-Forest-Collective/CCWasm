from os.path import abspath
import threading

try:
    from scarletio.ext import asyncio
except ImportError:
    print("WARNING: Scarletio could not be imported! Performance may be degraded!")

from computercraft import server

server.main()