"""
A scrapper for ygyl threads on /gif/ and /wsg/ on www.4chan.org .
"""

import basc_py4chan as basc
from subprocess import call

YGYL = ["ygyl", "YGYL", "Ygyl" ]
WEBM = ".webm"

def main():
    #boards_info()
    input("Will look for webms in /gif/ and /wsg/. Press enter to continue.")
    get_webms("wsg")
    get_webms("gif")
    

    
    pass

"""
Allows user to write links of files from a given board to a file.
Allows user to download files of a given board.
@param target_board_name the board of focus to look for ygyl threads.
"""
def get_webms( target_board_name):
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

"""
User decides whether or not to save file urls from the given board.
@param board_name name of board to save the files from.
@param file_urls the set of file urls intended to writted to a file.
"""
def save_links( board_name, file_urls):
    if not str( input( "Press enter to save webm links, enter anything else to not: " ) ):
        wf_name = str( input( 
            "File to save webm links to. Press enter to save to webms.txt: " ))
        if not wf_name:
            wf_name = "webms.txt"
        write_links( wf_name, board_name, WEBM, file_urls )
    if not str( input( "Press enter to save non-webm links, enter anything else to not: ") ):
        nwf_name = str( input(
            "File to save non-webms to. Press enter to save to others.txt:"
        ))
        if not nwf_name:
            nwf_name = "others.txt"    
        write_links( nwf_name, board_name, "", file_urls )


"""
Writes files of extension type file_ext to a file named file_name.
@param file_name the name of file to save file url to.
@param board_name the name of the current board where the files are located.
@param file_ext the file extension for the files of interest. "" for non-webms.
@param file_urls a dictionary of file extensions to lists of files with that file type.
"""
def write_links( file_name, board_name, file_ext, file_urls ):
    FILE_MODE = "a"
    url_file = open( file_name, FILE_MODE )

    links_being_written = "webm" if file_ext == WEBM else "non-webm"
    print("Writing "+links_being_written+" links to "+file_name+"...")

    url_file.write("/"+board_name+"/:\n")

    f_u = {}
    if file_ext == WEBM:
        f_u = { WEBM: file_urls[WEBM]}
    else:
        f_u = file_urls
        f_u.pop(WEBM)

    for file_ext in f_u.keys():
            url_file.write("\t"+file_ext+":\n")
            for f in f_u[file_ext]:
                url_file.write("\t\t"+f+"\n")
    
    url_file.close()

"""

"""
def to_download( board_name, files_from_posts ):
    for ext in files_from_posts.keys():
        to_d = str( input( "Press enter to download ALL "+ext+" files from "+board_name+". Enter anything else to not." ))
        if not to_d:
            for f in files_from_posts[ext]:
                file_location = f.file_url
                save_location = f.filename_original
                call(["curl", file_location, "--output", save_location])


"""

"""
def f_o_dict( file_set ):
    fo_dict = {}
    for f in file_set:
        if f.file_extension not in fo_dict.keys(): # file ext not contained
            fo_dict[f.file_extension] = [f]
        else: # file ext contained in f_d
            fo_dict[f.file_extension] += [f]
    return fo_dict

"""

"""
def file_url_dict( file_set ):
    f_d = {}
    for f in file_set:
        if f.file_extension not in f_d.keys(): # file ext not contained
            f_d[f.file_extension] = [f.file_url]
        else: # file ext contained in f_d
            f_d[f.file_extension] += [f.file_url]
    return f_d

"""
Function that checks for variations of 'ygyl' in a post. Checks in the post's subject and body.
@return whether or not ygyl is contained in the post.
"""
def search_for_ygyl( op_post ):
    subject = op_post.subject if op_post.subject else ""
    body_text = op_post.text_comment if op_post.text_comment else ""
    op_text = subject+body_text
    return any( ygyl_check in op_text for ygyl_check in YGYL)

main()