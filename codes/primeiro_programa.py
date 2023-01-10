# Import
import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text('Hello, world!')],
    [sg.Button('Ok')]
]

# Janela
janela = sg.Window('Título', layout)

# Loop de eventos
evento, valor = janela.read()

# Fechar
janela.close()