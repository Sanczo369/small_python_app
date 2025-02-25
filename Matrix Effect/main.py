import curses
import random
import signal
import sys
import time

# A signal handler function to handle interrupts
def signal_handler(sig, frame):
    curses.endwin()
    sys.exit(0)