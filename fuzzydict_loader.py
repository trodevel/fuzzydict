#!/usr/bin/python3

'''
fuzzydict Loader.

Copyright (C) 2023 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

import sys
import csv
import os

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from fuzzydict import fuzzydict
    from fuzzydict import fuzzydict_elem
else:
    # uses current package visibility
    from fuzzydict.fuzzydict import fuzzydict
    from fuzzydict.fuzzydict import fuzzydict_elem

##########################################################

def load_elem_v_1( data: list, filename: str ) -> fuzzydict_elem:

    if len( data ) != 2:
        raise Exception( f"load_v_1: broken record in {filename}: expected 2 fields, {len(data)} is given" )

    key                 = data[0]
    val                 = data[1]

    return fuzzydict_elem( key, val )

##########################################################

def load_v_1( csvfile, filename: str, is_caseinsensitive: bool ) -> fuzzydict:

    res = fuzzydict( is_caseinsensitive )

    reader = csv.reader( csvfile, delimiter=';' )

    for row in reader:

        elem = load_elem_v_1( row, filename )

        res.insert_elem_loaded( elem )

    #print( "INFO: read {} records from {} (v1)".format( len( res ), filename ) )

    return res

##########################################################

def load_inverse_w_synonyms_v_1( csvfile, filename: str, is_caseinsensitive: bool ) -> fuzzydict:

    res = fuzzydict( is_caseinsensitive )

    reader = csv.reader( csvfile, delimiter=';' )

    for row in reader:

        elem = load_elem_v_1( row, filename )

        res.insert_elem_loaded( elem )

    #print( "INFO: read {} records from {} (v1)".format( len( res ), filename ) )

    return res

##########################################################

def load( filename, is_caseinsensitive: bool = False ):

    with open( filename ) as csvfile:
        return load_v_1( csvfile, filename, is_caseinsensitive )

##########################################################

def load_inverse_w_synonyms( filename, is_caseinsensitive: bool = False ):

    with open( filename ) as csvfile:
        return load_inverse_w_synonyms_v_1( csvfile, filename, is_caseinsensitive )

##########################################################

def save_elem_v_1( elem: fuzzydict_elem, ffile, filename: str ):

    line = f"{elem.key};{elem.val}\n"

    ffile.write( line )

##########################################################

def save_direct( fuzzydict, filename ):

    f = open( filename, "w" )

    i = 0

    for s in fuzzydict.elems:
        save_elem_v_1( s, f, filename )
        i += 1

    return i

##########################################################

def save( fuzzydict, filename ):

    filename_new = filename + ".new"

    size = save_direct( fuzzydict, filename_new )

    filename_old = filename + ".old"

    if os.path.isfile( filename ):
        os.rename( filename, filename_old )
    os.rename( filename_new, filename )

    return size

##########################################################

def test_01():
    fuzzydict = load( "samples/sample_01.csv" )

    print( f"test_01: {fuzzydict}" )

def test_02():
    try:
        load( "samples/broken_sample_01.csv" )
    except Exception as e:
        print( f"test_02: exception: {e}" )

def test_03():
    try:
        load( "samples/broken_sample_02.csv" )
    except Exception as e:
        print( f"test_03: exception: {e}" )

def test_04():
    fuzzydict = load( "samples/sample_02.csv" )

    print( f"test_04: {fuzzydict}" )

def test_05():
    fuzzydict = load( "samples/sample_02.csv" )

    filename = "samples/sample_02.copy.csv"

    size = save( fuzzydict, filename )

    print( f"test_05: saved {size} records to {filename}" )

##########################################################

def test():

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
