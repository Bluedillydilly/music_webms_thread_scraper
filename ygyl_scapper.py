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
    get_webms()
    
    pass

def get_webms():
    target_boards = [ basc.Board(name) for name in target_boards_names ]
    print( target_boards )

    all_threads = [ board.get_all_threads() for board in target_boards ] 
    print( all_threads )
    print( all_threads[0])
    target_threads = [ thread for thread in all_threads[0] if search_for_ygyl( thread.topic ) ]
    print( "Threads containing ygyl:",target_threads )
    if not target_threads: # check if there are any threads those topic post contain "ygyl"
        print( " no ygyl threads ")
        return
    files = [ thread.files() for thread in target_threads ]
    print( files )
    ffiles = [ item for sublist in files for item in sublist ]
    print("_____________")
    print( ffiles )
    webms = [ file_name for file_name in ffiles if WEBM in file_name]
    webms_location = open("webms.txt", "w")
    for webm_name in webms:
        webms_location.write(webm_name+"\n")

    pass

def search_for_ygyl( op_post ):
    subject = op_post.subject if op_post.subject else ""
    body_text = op_post.text_comment if op_post.text_comment else ""
    op_text = subject+body_text
    print( op_text )
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