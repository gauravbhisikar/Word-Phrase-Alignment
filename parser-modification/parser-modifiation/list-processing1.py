#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_list = [[[["For"],[["example"]]],[","],[[["IBM"],["’s"],["Deep"],["Blue"]],[["chess"],["-"],["playing"],["system"]]],[["defeated"],[[[["world"],["champion"]],["Garry"],["Kasparov"]],[["in"],[["1997"]]]],[["-LRB-"],[["Hsu"]],[","],[["2002"]],["-RRB-"]]],["."]]]


def print_list(l):
    for i in l:
        if type(i) is list:
            if(len(i) > 1):
                print(i)
            print_list(i)


print_list(my_list)

