"""
    The Official Python GUI Programming with PySimpleGUI Course

    Window Types

    The 2 types of windows:
        1. One-Shot
        2. Persistent

    Persistent Windows have an "event loop"
"""

#
# One-shot Window
# Manually close the window
# Not typically written this way
#

import PySimpleGUI as sg

layout = [[sg.Text('This is our one-shot window')],
          [sg.Button('Ok')]]

window = sg.Window('Title', layout)

event, values = window.read()

window.close()

#
# One-shot Window
# Uses the close parameter to close window after first event
# This compresses the code by removing the need to call window.close()
# It's the normal definition of a "one-shot window"
#

layout = [[sg.Text('This is our one-shot window. close=True')],
          [sg.Button('Ok')]]

window = sg.Window('Title', layout)

event, values = window.read(close=True)


#
# One-shot Window
# Combining all parts into 1 line of code
# When you want to do it all in a single line, do these 2 things:
#   1. Define the layout in the Window call
#   2. "chain" the read call onto the call to create the Window
#

event, values = sg.Window('Title', [[sg.Text('This is our 1-line window')], [sg.Button('Ok')]]).read(close=True)


#
# Persistent Window
# This means a Window with an "Event Loop"
#
layout = [[sg.Text('This is our persistent window')],
          [sg.Button('1'), sg.Button('2'), sg.Button('Exit')]]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    # if event in (sg.WIN_CLOSED ,'Exit'):      # The "more pythonic" version
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '1':
        print('You clicked 1')
    elif event == '2':
        print('You clicked 2')

window.close()
