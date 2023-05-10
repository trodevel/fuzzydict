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

def load_inverse_w_synonyms_elem_v_1( data: list, filename: str ) -> list[fuzzydict_elem]:

    if len( data ) < 2:
        raise Exception( f"load_inverse_w_synonyms_v_1: broken record in {filename}: expected 2 or more fields, {len(data)} is given" )

    res: list[fuzzydict_elem] = []

    # first row contains an value
    val                 = data[0]

    for i in range( 1, len( data ) ):
        key  = data[i]
        elem = fuzzydict_elem( key, val )
        res.append( elem )

    return res

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

    i = 0

    for row in reader:

        i += 1

        elems = load_inverse_w_synonyms_elem_v_1( row, filename )

        for elem in elems:
            res.insert_elem_loaded( elem )

    print( "INFO: read {}/{} lines/records from {} (v1)".format( i, len( res ), filename ) )

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
