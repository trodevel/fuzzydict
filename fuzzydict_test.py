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

def test():

    test_01()
    test_02()

##########################################################

if __name__ == "__main__":
   test()

##########################################################
