import time
import sys
from colorama import Fore

print(Fore.GREEN, end = '')

def printTime(str, delay):
    sys.stdout.write(f"\033[F\r{str}\n{str}")
    sys.stdout.flush()
    time.sleep(delay)

printTime("Connection", 0.3)
printTime("Connection .", 0.3)
printTime("Connection ..", 0.3)
printTime("Connection ...", 0.7)
printTime("Connection success", 1.0)
printTime("Hello", 1.0)
printTime("Neo?", 10.0)
printTime("Are you here?", 5.0)
printTime("Find white rabbit", 10.0)
printTime("Knock, knock, Neo!", 1.0)