"""
    File containing various helper functions for ygyl_scraper.py
"""

import urllib.request

YGYL = ["ygyl", "YGYL", "Ygyl" ]



def more_info():
    """
    Prints more info about the program.
    Prints info about configuration customization.
    """
    lines = "------------------------------------------"
    print(lines+"\nAdditional Information\n"+lines)
    print("Configuration:")
    print("\tEdit WEBM global variable to change target file type.")
    print("\tEdit YGYL global variable to change ygyl phrases to be search for. Located in ygyl_helper.")
    print("\tEdit BOARD_LIST global variable to change boards that get search. ")
    print(lines+"\n")


def search_for_ygyl( op_post ):
    """
    Function that checks for variations of 'ygyl' in a post. Checks in the post's subject and body.
    @return whether or not ygyl is contained in the post.
    """
    subject = op_post.subject if op_post.subject else ""
    body_text = op_post.text_comment if op_post.text_comment else ""
    op_text = subject+body_text
    return any( ygyl_check in op_text for ygyl_check in YGYL)



def file_url_dict( file_set ):
    """
    Constructs a dictionary of file extensions to file url key-value pairs
    @param file_set the set of files to create the dictionary from
    @return f_d a file dictionary of file extensions to file urls
    """
    f_d = {}
    for f in file_set:
        if f.file_extension not in f_d.keys(): # file ext not contained
            f_d[f.file_extension] = [f.file_url]
        else: # file ext contained in f_d
            f_d[f.file_extension] += [f.file_url]
    return f_d


def f_o_dict( file_set ):
    """
    Constructs a dictionary of file extension to files key-value pairs.
    @param file_set the list of files to generate the dictionary from.
    @return fo_dict the completed dictionary of file extensions to files
    """
    fo_dict = {}
    for f in file_set:
        if f.file_extension not in fo_dict.keys(): # file ext not contained
            fo_dict[f.file_extension] = [f]
        else: # file ext contained in f_d
            fo_dict[f.file_extension] += [f]
    return fo_dict


def to_download( board_name, files_from_posts ):
    """

    """
    for ext in files_from_posts.keys():
        to_d = str( input( "Press enter to download ALL "+ext+" files from "+board_name+". Enter anything else to not." ))
        if not to_d:
            for f in files_from_posts[ext]:
                file_location = f.file_url
                save_location = f.filename_original
                urllib.request.urlretrieve( file_location, save_location )
