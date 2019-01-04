"""
A scrapper for ygyl threads on /gif/ and /wsg/ on www.4chan.org .
"""

import basc_py4chan as basc
import json as js

target_boards_names = ['wsg'] # boards of interest

YGYL = ["ygyl", "YGYL", "Ygyl" ]
WEBM = ".webm"

def main():
    #boards_info()
    get_webms("wsg")
    
    pass

def get_webms( target_board_name):
    print( "Board of focus: "+target_board_name )
    all_threads = basc.Board(target_board_name).get_all_threads() 
    target_threads = [ thread for thread in all_threads if search_for_ygyl( thread.topic ) ]
    print( "Threads containing ygyl:",target_threads )
    if not target_threads: # check if there are any threads those topic post contain "ygyl"
        print( "No current ygyl threads in /"+target_board_name+"/.")
        return
    all_target_posts = []
    for thread in target_threads:
        thread_files = thread.all_posts
        all_target_posts+=thread_files
    print( all_target_posts[0] )
    posts_files = [ post.file for post in all_target_posts if post.has_file]
    print( posts_files)

    files_dictionary = file_dict( posts_files )
    print( files_dictionary )
    print( files_dictionary.keys() )

    webms_location = open("webms.txt", "w")
    other_files_location = open("others.txt", "w")
    for post_file in posts_files:
        if post_file.file_extension == WEBM:
            webms_location.write( post_file.file_url +"\n")

    # create dictionary of file extension, list of files with that extension pairs

def file_dict( file_set ):
    f_d = {}
    for f in file_set:
        if f.file_extension not in f_d.keys(): # file ext not contained
            f_d[f.file_extension] = [f.file_url]
        else: # file ext contained in f_d
            f_d[f.file_extension] += [f.file_url]
    return f_d

def search_for_ygyl( op_post ):
    subject = op_post.subject if op_post.subject else ""
    body_text = op_post.text_comment if op_post.text_comment else ""
    op_text = subject+body_text
    return any( ygyl_check in op_text for ygyl_check in YGYL)

"""
Returns information related to a set of boards.
I plan on expanding on board analysis later, webms are of focus now.
"""
def boards_info():
    global b_info 
    b_info = 0 # board info

    f = open('boards.json')
    b_info = js.load( f )
    print( b_info )
    print( b_info.keys() )

    # empty list. Will contain exclude keys and their value
    ex_info = [] 
    
    # keys to pop. Information not relevant to my purposes
    ex_keys = ['troll_flags']
    ex_info = pop_ex( ex_keys )

    print( ex_info )
    print( b_info.keys())
    b_info = b_info['boards']
    for board in b_info:
        print(board) # print each board information out seperately

    pass

def pop_ex( ex_keys ):
    global b_info
    ex_info = []
    for key in ex_keys:
        ex_info.append( { key : b_info.pop(key) } )
    return ex_info

main()