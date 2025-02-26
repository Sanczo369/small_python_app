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

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Get the maximum y and x coordinates of the screen
    max_y, max_x = stdscr.getmaxyx()

    # Initialize a list to keep track of the current position of characters in each column
    columns = [0] * max_x

    # Main loop for the matrix rain effect
    while True:
        # Clear the screen
        stdscr.clear()