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
        return self.key + "=" + str( self.val )

##########################################################

class fuzzydict:

    elems: list               = None
    is_caseinsensitive: bool  = None

    def __init__( self, is_caseinsensitive = False ):
        self.elems = []
        self.is_caseinsensitive = is_caseinsensitive

    def __str__(self):
        res = ""
        for e in self.elems:
            if res:
                res += ";"
            res += str( e )
        return res

    def __len__( self ):
        return len( self.elems )

    def exists( self, kkey: str, similarity_pct: int = 100 ) -> bool:

        key = self._adjust_key( kkey )

        for e in self.elems:
            if self._is_similar( key, e.key, similarity_pct ):
                return True
        return False

    def insert( self, kkey: str, val ) -> bool:
        return self._insert( self._adjust_key( kkey ), val, False )

    def insert_elem( self, elem: fuzzydict_elem ) -> bool:
        return self._insert( self._adjust_key( elem.key ), elem.val, False )

    def insert_elem_loaded( self, elem: fuzzydict_elem ) -> bool:
        return self._insert( self._adjust_key( elem.key ), elem.val, True )

    def delete( self, kkey: str ) -> bool:

        key = self._adjust_key( kkey )

        i = 0

        for e in self.elems:
            if key == e.key:
                del self.elems[i]
                return True
            i += 1

        return False

    def find_all_elems( self, kkey: str, similarity_pct: int ) -> list:
        return self._find_all_elems( self._adjust_key( kkey ), similarity_pct )

    def find_all( self, kkey: str, similarity_pct: int ) -> list:

        res = []

        elems = self._find_all_elems( self._adjust_key( kkey ), similarity_pct )

        for e in elems:
            res.append( e.val )

        return res

    def find_best_elem( self, kkey: str, similarity_pct: int ) -> ( bool, fuzzydict_elem ):
        return self._find_all_elems( self._adjust_key( kkey ), similarity_pct )

    def find_best( self, kkey: str, similarity_pct: int ):
        has_found, elem = self._find_best_elem( self._adjust_key( kkey ), similarity_pct )

        if has_found:
            return ( True, elem.val )

        return ( False, None )

    def _adjust_key( self, key: str ) -> str:
        if self.is_caseinsensitive:
            return key.lower()
        return key

    def _insert( self, key: str, val, is_loaded: bool ) -> bool:
        if is_loaded == False and self.exists( key ):
            return False

        e = fuzzydict_elem( key, val )

        self.elems.append( e )

        return True

    def _find_all_elems( self, key: str, similarity_pct: int ) -> list:

        res = []

        for e in self.elems:
            if self._is_similar( key, e.key, similarity_pct ):
                res.append( e )

        return res

    def _find_best_elem( self, key: str, similarity_pct: int ) -> ( bool, fuzzydict_elem ):

        has_found = False
        elem      = None

        current_max = 0

        for e in self.elems:
            ratio = self._ratio( key, e.key )
            if ratio >= similarity_pct and ratio > current_max:
                current_max = ratio
                has_found   = True
                elem        = e

        return ( has_found, elem )

    def _is_similar( self, s1: str, s2: str, similarity_pct: int ) -> bool:
        ratio = self._ratio( s1, s2 )
        if ratio >= similarity_pct:
            return True
        return False

    def _ratio( self, s1: str, s2: str ):
        return fuzz.ratio( s1, s2 )

##########################################################
