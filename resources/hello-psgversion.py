import PySimpleGUI as sg

sg.main()


layout = [[sg.Button('Hello World\n(click me)', size=(10,2))],
          [sg.Button('QUIT', button_color=('red',None))]]

window = sg.Window('', layout, element_justification='center')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'QUIT'):
        break
    if event == 'Hello World\n(click me)':
        print("hi there, everyone!")

window.close()
