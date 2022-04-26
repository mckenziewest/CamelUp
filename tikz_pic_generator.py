# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:31:15 2022

@author: WESTMR
"""
def get_coordinate(color,x,y):
    color_coordinate_dict = {"Blue":"(B)","Red":"(R)","Green":"(G)", "Purple":"(P)", "Yellow":"(Y)"}
    coord_string = "\coordinate "
    coord_string += color_coordinate_dict[color]
    coord_string += f" at ({2*x+1/2},{y/2})"
    return coord_string
def gen_picture(start_position):
    picture_string = "\\begin{tikzpicture}"
    for color,x,y in zip(*start_position):
        picture_string += f"\n\t{get_coordinate(color,x,y)};"
    color_coordinate_dict = {"Blue":"(B)","Red":"(R)","Green":"(G)", "Purple":"(P)", "Yellow":"(Y)"}
    for key,value in color_coordinate_dict.items():
        picture_string += f"\n\t\\node at {value} {{\\color{{{key}}} {key}}};"
    picture_string += "\n\t\\foreach\\x in {1,2,3}"
    picture_string += "\n\t\t\\draw (2*\\x,0) -- ++(1,0) node[midway, below] {$\\x$};"
    picture_string += "\n\\end{tikzpicture}"
    return picture_string


all_positions = [
    [['Blue', 'Red', 'Green', 'Purple', 'Yellow'], [2, 2, 1, 1, 1], [2, 1, 3, 2, 1]],
    [['Red','Blue',  'Green', 'Purple', 'Yellow'], [3, 2, 1, 1, 1], [1, 1, 3, 2, 1]]
    ]

def gen_all_pictures(all_positions):
    string_of_tikz = ""
    string_of_tikz += "\\definecolor{Blue}{RGB}{13, 41, 255}"
    string_of_tikz += "\n\\definecolor{Red}{RGB}{255, 51, 5}"
    string_of_tikz += "\n\\definecolor{Green}{RGB}{27, 148, 37}"
    string_of_tikz += "\n\\definecolor{Purple}{RGB}{101, 24, 173}"
    string_of_tikz += "\n\\definecolor{Yellow}{RGB}{201, 195, 18}"
    for position in all_positions:
        string_of_tikz += "\n\n"
        string_of_tikz += gen_picture(position)
    return string_of_tikz

with open("tikz_pics.txt",'w') as the_file:
    the_file.write(gen_all_pictures(all_positions))