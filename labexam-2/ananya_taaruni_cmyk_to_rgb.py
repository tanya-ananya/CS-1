'''
This program takes in CMYK color values and translates them to RGB and outputs tot he user
Author: Taaruni Ananya
'''

user_input = ''

print('CMYK To RGB Converter\n')



def CMYK_To_RGB(cyan=0, magenta=0, yellow=0, key=0):
    cmyk = []
    rgb = []

    cmyk['cyan'] = cyan
    cmyk['magenta'] = magenta
    cmyk['yellow'] = yellow
    cmyk['key'] = key

    red = 255 * (1 - (cyan/100)) * (1 - (key/100))
    green = 255 * (1 - (magenta/100)) * (1 - (key/100))
    blue = 255 * (1 - (yellow/100)) * (1 - (key/100))

    rgb['red'] = int(red)
    rgb['green'] = int(green)
    rgb['blue'] = int(blue)

    for x, y in rgb.items():
        color_name = x
        color_number = y
        return print(f'{color_name} : {color_number}')


while user_input.lower() != 'q' or 'quit':
    cy = int(input('Enter the Cyan Color Value: '))
    mag = int(input('Enter the Magenta Color Value: '))
    yel = int(input('Enter the Yellow Color Value: '))
    ky = int(input('Enter the Key Color Value: '))

    CMYK_To_RGB(cyan=cy, magenta=mag, yellow=yel, key=ky)

    user_input = input("Hit enter if you want to continue or type 'q'/'quit' to quit\n")



    