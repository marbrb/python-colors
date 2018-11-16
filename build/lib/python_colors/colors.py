#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Main module."""

from functools import partial


class Coloring:
    '''Class for print colored text on UNIX terminals on a easy way, available
    colors are: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE
    '''

    default_property = 'BLACK'

    properties = {
        'BLACK':  '\033[90m',
        'RED':  '\033[91m',
        'GREEN':  '\033[92m',
        'YELLOW':  '\033[93m',
        'BLUE':  '\033[94m',
        'PURPLE':  '\033[95m',
        'CYAN':  '\033[96m',
        'WHITE':  '\033[97m',
    }

    end_color = '\033[0m'

    @classmethod
    def colored_text(self, text, color):
        return '{color}{text}{end_color}'.format(
            color=color,
            text=text,
            end_color=self.end_color
        )

    @classmethod
    def make_color_function(self, color):
        default = self.default_property
        color = self.properties.get(color, self.properties[default]) # default BLACK
        return partial(self.colored_text, color=color)

class Styling(Coloring):
    default_property = 'BOLD'

    properties = {
        'BOLD': '\033[1m'
    }

black = Coloring.make_color_function('BLACK')
red = Coloring.make_color_function('RED')
green = Coloring.make_color_function('GREEN')
yellow = Coloring.make_color_function('YELLOW')
blue = Coloring.make_color_function('BLUE')
purple = Coloring.make_color_function('PURPLE')
cyan = Coloring.make_color_function('CYAN')
white = Coloring.make_color_function('WHITE')

bold = Styling.make_color_function('BOLD')
