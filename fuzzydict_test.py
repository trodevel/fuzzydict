#!/usr/bin/python3

'''
fuzzydict test.

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

##########################################################

def create_dict_01():

    d = fuzzydict.fuzzydict()

    d.insert( "developer", 1 )
    d.insert( "backend developer", 2 )
    d.insert( "frontend developer", 3 )
    d.insert( "python developer", 4 )
    d.insert( "manager", 5 )

    return d

##########################################################

def to_string_fuzzydict_list( l : list ):
    res = ""
    for v in l:
        if res:
            res += ","
        res += str( v )
    return res

##########################################################

def test_01():

    d = create_dict_01()

    print( f'test_01: {d}' )

##########################################################

def test_02():

    d = create_dict_01()

    word = "developer"

    has_found = d.exists( word )

    print( f"test_02: word '{word}', is found = {has_found} - {d}" )

##########################################################

def test_02():

    d = create_dict_01()

    word = "developer"

    has_found = d.exists( word )

    print( f"test_02: word '{word}', is found = {has_found} - {d}" )

##########################################################

def test_03():

    d = create_dict_01()

    word = "developerx"

    has_found = d.exists( word )

    print( f"test_03: word '{word}', is found = {has_found} - {d}" )

##########################################################

def test_04():

    d = create_dict_01()

    word = "developer"

    print( f"test_04: before: {d}" )

    has_deleted = d.delete( word )

    print( f"test_04: after : {d}" )

    print( f"test_04: word '{word}', has deleted = {has_deleted}" )

##########################################################

def test_05():

    d = create_dict_01()

    word = "developerx"

    print( f"test_05: before: {d}" )

    has_deleted = d.delete( word )

    print( f"test_05: after : {d}" )

    print( f"test_05: word '{word}', has deleted = {has_deleted}" )

##########################################################

def test_06():

    d = create_dict_01()

    word = "developer"
    similarity = 75

    print( f"test_06: data: {d}" )

    res = d.find_all_elems( word, similarity )

    print( f"test_06: word '{word}', similarity {similarity}, matches = {len(res)}, {to_string_fuzzydict_list(res)}" )

##########################################################

def test_07():

    d = fuzzydict.fuzzydict()

    d.insert_elem( fuzzydict.fuzzydict_elem( "developer", 1 ) )

    print( f'test_07: {d}' )

##########################################################
def test():

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()
    test_07()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
