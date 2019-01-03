"""
A scrapper for ygyl threads on /gif/ and /wsg/ on www.4chan.org .
"""

import basc_py4chan as basc
import json as js

def main():
    boards_info()
    pass

def boards_info():
    f = open('boards.json')
    b_info = js.load( f )
    print( b_info )
    print( b_info.keys() )

    # empty list. Will contain exclude keys and their value
    ex_info = [] 
    
    # keys to pop. Information not relevant to my purposes
    ex_keys = ['troll_flags']
    for key in ex_keys:
        ex_info.append( { key : b_info.pop(key) } )
    print( ex_info )


    pass

main()