import curses
import random
import signal
import sys
import time

# A signal handler function to handle interrupts
def signal_handler(sig, frame):
    curses.endwin()
    sys.exit(0)


# Main function
def main(stdscr):
    # Hide the cursor
    curses.curs_set(0)
