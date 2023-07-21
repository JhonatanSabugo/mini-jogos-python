import PySimpleGUIQt as sg
import adivinhacao

layout_principal = [
    [
        sg.Text(adivinhacao.mensagem_boas_vindas(), font='Arial', text_color='White', background_color='Black')
    ]
]

view_principal = sg.Window(
    "Mini Jogos em Python",
    layout= layout_principal,
    size=(300,200),
    element_justification='c'
)

while True:
    event, values = view_principal.read()
    if event == sg.WIN_CLOSED:
        break

view_principal.close()