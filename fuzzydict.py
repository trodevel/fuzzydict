#!/usr/bin/python3

'''
fuzzydict.

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

from thefuzz import fuzz

##########################################################

class fuzzydict_elem:
    key: str                  = None
    val                       = None

    def __init__( self, key: str, val ):
        self.key = key
        self.val = val

    def __str__( self ):
        return self.key + "=" + str( self.value )

##########################################################

class fuzzydict:

    elems: list               = None

    def __init__( self ):
        pass

    def __str__(self):
        res = ""
        for e in self.elems:
            if res:
                res += ";"
            res += e
        return res

##########################################################
