"""
A scrapper for ygyl threads on /gif/ and /wsg/ on www.4chan.org .
"""

import basc_py4chan as basc
import json as js
from subprocess import call

YGYL = ["ygyl", "YGYL", "Ygyl" ]
WEBM = ".webm"

def main():
    #boards_info()
    input("Will look for webms in /gif/ and /wsg/. Press enter to continue.")
    get_webms("wsg")
    get_webms("gif")
    

    
    pass

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

    wf_name = str( input( 
        "File to save webm links to. Press enter to save to webms.txt: " ))
    if not wf_name:
        wf_name = "webms.txt"
    nwf_name = str( input(
        "File to save non-webms to. Press enter to save to others.txt:"
    ))
    if not nwf_name:
        nwf_name = "others.txt"

    webms_location = open( wf_name, "a" )
    other_files_location = open( nwf_name, "a" )
    
    print( "Writing webm links to "+wf_name+"...")
    webms_location.write("/"+target_board_name+"/:\n")
    for post_file in files_url_dictionary[WEBM]:
            webms_location.write( "\t"+post_file +"\n")
    webms_location.close()
    
    print("Writing non-webm links to "+nwf_name+"...")
    other_files_location.write("/"+target_board_name+"/:\n")
    for file_ext in files_url_dictionary.keys():
        if file_ext != WEBM:
            other_files_location.write("\t"+file_ext+":\n")
            for f in files_url_dictionary[file_ext]:
                other_files_location.write("\t\t"+f+"\n")
    other_files_location.close()

    to_download( target_board_name, files_object_dictionary)


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

"""
def search_for_ygyl( op_post ):
    subject = op_post.subject if op_post.subject else ""
    body_text = op_post.text_comment if op_post.text_comment else ""
    op_text = subject+body_text
    return any( ygyl_check in op_text for ygyl_check in YGYL)

main()