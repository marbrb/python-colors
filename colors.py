#! /usr/bin/python3
from functools import partial

# description: Print colored text on UNIX terminals
# package-name: python-colors
# import-name: colors

class Coloring(object):
    '''
    Class for print colored text on UNIX terminals on a easy way, available
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
red = Coloring.make_color_function('RED')
green = Coloring.make_color_function('GREEN')
yellow = Coloring.make_color_function('YELLOW')
blue = Coloring.make_color_function('BLUE')
purple = Coloring.make_color_function('PURPLE')
cyan = Coloring.make_color_function('CYAN')
white = Coloring.make_color_function('WHITE')


if __name__ == '__main__': # just for test
    print(green('hola'))
    print(black('hola'))
    print(red('hola'))
    print(blue('hola'))
    print(yellow('hola'))
    print(white('hola'))
    print(purple('hola'))
    print(cyan('hola'))
