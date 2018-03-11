#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Main module."""

from functools import partial


class Coloring:
    '''Class for print colored text on UNIX terminals on a easy way, available
    colors are: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE
    '''
    colors = {
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
        color = self.colors.get(color, self.colors['BLACK']) # default BLACK
        return partial(self.colored_text, color=color)


black = Coloring.make_color_function('BLACK')
black.__doc__ = 'function to print black text.'
red = Coloring.make_color_function('RED')
red.__doc__ = 'function to print red text.'
green = Coloring.make_color_function('GREEN')
green.__doc__ = 'function to print green text.'
yellow = Coloring.make_color_function('YELLOW')
yellow.__doc__ = 'function to print yellow text.'
blue = Coloring.make_color_function('BLUE')
blue.__doc__ = 'function to print blue text.'
purple = Coloring.make_color_function('PURPLE')
purple.__doc__ = 'function to print purple text.'
cyan = Coloring.make_color_function('CYAN')
cyan.__doc__ = 'function to print cyan text.'
white = Coloring.make_color_function('WHITE')
white.__doc__ = 'function to print white text.'
