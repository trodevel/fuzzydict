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

import fuzzydict
from fuzzydict_loader import load, save

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

def test_06():
    fuzzydict = load( "samples/sample_03.csv" )

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
