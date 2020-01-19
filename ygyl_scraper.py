"""
A scraper for ygyl threads on /gif/ and /wsg/ on www.4chan.org .
"""
#imports
import basc_py4chan as basc
import json
from sys import argv

# local imports
from ygyl_helper import *
from config import BOARD_LIST, FILE_EXTS

def main():
    """

    """
    options = argv[1:]

    #boards_info()
    print( "Will look for webms and other file formats in various 4chan boards. \
        \nRun like `python3 ygyl_scraper.py H` to list help." )

    # check what options used
    if "H" in options:
        more_info() 
    
    for board in BOARD_LIST:
        if str(input("Search /"+board+"/ for files?(Y for yes) ")) == "Y":
            search_board(board)
    


def search_board( target_board_name):
    """
    Allows user to write links of files from a given board to a file.
    Allows user to download files of a given board.
    @param target_board_name the board of focus to look for ygyl threads.
    """
    print( "Board of focus: "+target_board_name )
    all_threads = basc.Board(target_board_name).get_all_threads() 
    target_threads = [ thread for thread in all_threads if search_for_ygyl( thread.topic ) ]
    if not target_threads: # check if there are any threads those topic post contain "ygyl"
        print( "No current ygyl threads in /"+target_board_name+"/.")
        return
    all_target_posts = []
    for thread in target_threads:
        thread_files = thread.all_posts
        all_target_posts+=thread_files
    files_from_posts = [ post.file for post in all_target_posts if post.has_file]

    files_object_dictionary = f_o_dict( files_from_posts )
    files_url_dictionary = file_url_dict( files_from_posts )

    save_links( target_board_name, files_url_dictionary)
   
    to_download( target_board_name, files_object_dictionary)


def save_links( board_name, file_urls):
    """
    User decides whether or not to save file urls from the given board.
    @param board_name name of board to save the files from.
    @param file_urls the set of file urls intended to writted to a file.
    """
    # check to write file urls to a file
    if str( input( "Enter Y to save", FILE_EXTS, "links, enter anything else to not: " ) ) == "Y":
        wf_name = str( input( 
            "File to save webm links to (press enter to save to webms.txt): " ))
        if not wf_name:
            wf_name = "webms.txt"
        write_links( wf_name, board_name, FILE_EXTS, file_urls )


def write_links( file_name, board_name, file_ext, file_urls ):
    """
    Writes files of extension type file_ext to a file named file_name.
    @param file_name the name of file to save file url to.
    @param board_name the name of the current board where the files are located.
    @param file_ext the file extension for the files of interest. "" for non-webms.
    @param file_urls a dictionary of file extensions to lists of files with that file type.
    """
    links_being_written = "webm" if file_ext == FILE_EXTS else "non-webm"
    print("Writing "+links_being_written+" links to "+file_name+"...")

    f_u = { board_name:"" }
    if file_ext == FILE_EXTS:
        f_u[board_name] = { FILE_EXTS: file_urls[FILE_EXTS]}
    else:
        f_u = file_urls
        f_u.pop(FILE_EXTS)

    with open(file_name, "a") as output_file:
        json.dump( f_u, output_file )




main()