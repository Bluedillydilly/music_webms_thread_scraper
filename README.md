# Music Webms Thread Scraper
A 4chan scraper, using basc-py4chan, that gathers webms from YGYL threads.
Follow commandline prompts once ran.
NOTES:
- YGYL threads are assumed to be threads that contain variants of "YGYL" in the body or subject of OP's post. 
Due to this, non-YGYL threads may be used as they could contain wording such as "...all I see are YGYL threads, let's get a X thread started". 

## Current features:
    - Allows user to download any file, or specifically webms, from /wsg/ and /gif/
        - User can choose between webm and/or non-webm files 
    - Allows user to write url of all files, organized by board, then file type, from /wsg/ and /gif/ to a file

## Possible additions:
    - allow user to select what board(s) to choose from
    - allow user to select what file type(s) to save
    - allow user to select what keyword(s) to search for

## Required to run:
    - basc-py4chan module. Look at https://github.com/bibanon/BASC-py4chan for more information and installation instructions
    - only tested on python 3.6.7 . Will probably work on most 3.x. Let me know if any problems occur
