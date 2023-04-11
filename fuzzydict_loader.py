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

import fuzzydict       # Ad


##########################################################

def load_elem_v_1( data: list, filename: str ) -> fuzzydict.fuzzydict_elem:

    if len( data ) != 2:
        raise Exception( f"load_v_1: broken record in {filename}: expected 8 fields, {len(data)} is given" )

    key                 = data[0]
    val                 = data[1]

    return fuzzydict.fuzzydict_elem( key, val )

##########################################################

def load_v_1( csvfile, filename: str ) -> fuzzydict.fuzzydict:

    res = fuzzydict.fuzzydict()

    reader = csv.reader( csvfile, delimiter=';' )

    for row in reader:

        elem = load_elem_v_1( row, filename )

        res.insert_elem( elem )

    print( "INFO: read {} records from {} (v1)".format( len( res ), filename ) )

    return res

##########################################################

def load( filename ):

    with open( filename ) as csvfile:
        return load_v_1( csvfile, filename )

##########################################################

def save_direct( fuzzydict, filename ):

    f = open( filename, "w" )

    i = 0

    for s in fuzzydict.profiles:
        line = str( fuzzydict.profiles[s] ) + "\n"
        f.write( line )
        i += 1

    return i

##########################################################

def save_file( fuzzydict, filename ):

    filename_new = filename + ".new"

    size = save_direct( fuzzydict, filename_new )

    filename_old = filename + ".old"

    if os.path.isfile( filename ):
        os.rename( filename, filename_old )
    os.rename( filename_new, filename )

    print( "INFO: saved {} records to {}".format( size, filename ) )

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
    try:
        load( "samples/broken_sample_03.csv" )
    except Exception as e:
        print( f"test_04: exception: {e}" )

def test_05():
    try:
        load( "samples/broken_sample_04.csv" )
    except Exception as e:
        print( f"test_05: exception: {e}" )

def test_06():
    fuzzydict = load( "samples/sample_02.csv" )

    print( f"test_06: {fuzzydict}" )

##########################################################

def test():

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
