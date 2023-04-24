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
import fuzzydict_loader

##########################################################

gl_dict_02 = None
gl_dict_03 = None
gl_dict_04 = None

##########################################################

def create_dict_01():

    d = fuzzydict.fuzzydict( True )

    d.insert( "developer", 1 )
    d.insert( "backend developer", 2 )
    d.insert( "frontend developer", 3 )
    d.insert( "python developer", 4 )
    d.insert( "manager", 5 )

    return d

##########################################################

def create_dict_02():

    global gl_dict_02

    if not gl_dict_02:
        gl_dict_02 = fuzzydict_loader.load( 'samples/sample_01.csv' )
        gl_dict_02.set_caseinsensitive( True )

    return gl_dict_02

##########################################################

def create_dict_03():

    global gl_dict_03

    if not gl_dict_03:
        gl_dict_03 = fuzzydict_loader.load( 'samples/locations.eng.csv' )
        gl_dict_03.set_caseinsensitive( True )

    return gl_dict_03

##########################################################

def create_dict_04():

    global gl_dict_04

    if not gl_dict_04:
        gl_dict_04 = fuzzydict_loader.load( 'samples/locations.rus.csv' )
        gl_dict_04.set_caseinsensitive( True )

    return gl_dict_04

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

def test_find_all_elems( name: str, d: fuzzydict.fuzzydict, word: str, similarity: float ):

    res = d.find_all_elems( word, similarity )

    print( f"{name}: word '{word}', similarity {similarity}, matches = {len(res)}, {to_string_fuzzydict_list(res)}" )

##########################################################
def test_06():

    d = create_dict_02()

    test_find_all_elems( "test_06", d, "developer", 75 )
    test_find_all_elems( "test_06", d, "developr", 75 )
    test_find_all_elems( "test_06", d, "develpr", 75 )

##########################################################

def test_07():

    d = fuzzydict.fuzzydict()

    d.insert_elem( fuzzydict.fuzzydict_elem( "developer", 1 ) )

    print( f'test_07: {d}' )

##########################################################

def test_08():

    d = create_dict_02()

    test_find_all_elems( "test_08", d, "java", 75 )
    test_find_all_elems( "test_08", d, "Java", 75 )
    test_find_all_elems( "test_08", d, "jave", 75 )
    test_find_all_elems( "test_08", d, "jva", 75 )

##########################################################

def test_09():

    d = create_dict_02()

    test_find_all_elems( "test_09", d, "Git", 75 )
    test_find_all_elems( "test_09", d, "git", 75 )
    test_find_all_elems( "test_09", d, "gt", 75 )
    test_find_all_elems( "test_09", d, "Gt", 75 )

##########################################################

def test_10():

    d = create_dict_02()

    test_find_all_elems( "test_10", d, "GitHub", 75 )
    test_find_all_elems( "test_10", d, "github", 75 )

##########################################################

def test_11():

    d = create_dict_02()

    test_find_all_elems( "test_11", d, "frontend", 75 )

##########################################################

def test_12():

    d = create_dict_03()

    test_find_all_elems( "test_12", d, "Munich", 75 )
    test_find_all_elems( "test_12", d, "Munch", 75 )
    test_find_all_elems( "test_12", d, "Mnich", 75 )

##########################################################

def test_13():

    d = create_dict_03()

    test_find_all_elems( "test_13", d, "Munich", 85 )
    test_find_all_elems( "test_13", d, "Munch", 85 )
    test_find_all_elems( "test_13", d, "Mnich", 85 )

##########################################################

def test_14():

    d = create_dict_04()

    test_find_all_elems( "test_14", d, "Мюнхен", 75 )
    test_find_all_elems( "test_14", d, "мюнхен", 75 )
    test_find_all_elems( "test_14", d, "Мюнхн", 75 )
    test_find_all_elems( "test_14", d, "Mнхен", 75 )

##########################################################

def test():

    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()
    test_07()
    test_08()
    test_09()
    test_10()
    test_11()
    test_12()
    test_13()
    test_14()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
