"""
	Configuration File for ygyl scraper.
	Various option to alter how it performs and such
	idk my dude, I'm trying to organize customizable stuff better.
"""

# Words to look for to decide if the thread is an YGYL thread
# If the OP of the thread contains any of the `TARGET_WORDS` that thread is considered
# an YGYL thread.
TARGET_WORDS = ["ygyl", "YGYL", "Ygyl" ]
YGYL = TARGET_WORDS


# List of boards to search in for YGYL threads
# Check look else for complete list to choose from
BOARD_LIST = ["wsg", "gif"]


# File extensions to look for
# If a file contains such an extension it is to be targeted
FILE_EXTS = [".webm"]


# Signifies an option
# 
CLI_OPT = "-"