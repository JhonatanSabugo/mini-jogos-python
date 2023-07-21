import PySimpleGUI as sg
import adivinhacao

numero = adivinhacao.numero_secreto()
rodada= 1 
total_de_tentativas= adivinhacao.selecao_nivel
pontos = 500
chute = 0

layout_principal = [
    [
        sg.Text(adivinhacao.mensagem_boas_vindas(), font='Arial', text_color='White', background_color='Black')
    ],

    [
        sg.Text("Escolha um nível: ", font='Arial')
    ],

    [
        sg.Button("Facíl", key='-BT_EASY-' , font='Arial'),
        sg.Button("Médio", key='-BT_MEDIUM-' ,font='Arial'),
        sg.Button("Difícil", key='-BT_HARD-' ,font='Arial')
    ]
]

layout_jogo = [
    [
        sg.Text(f"Tetativa {rodada} de {total_de_tentativas}", font='Arial')
    ],

    [
        sg.Text("Digite um numero de 1 a 100: ", font='Arial') , sg.Input(font='Arial', key='-CHUTE-')
    ],

    [
        sg.Text("")
    ]
]


view_principal = sg.Window(
    "Mini Jogos em Python",
    layout= layout_principal,
    size=(300,200),
    icon=('assets/logo.ico'),
    element_justification='c'
)

view_jogo = sg.Window(
    "Jogando Adivinhação",
    layout= layout_jogo,
    size=(300,200),
    element_justification='c'
)

while True:
    event, values = view_principal.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == '-BT_EASY-':
        values = 1
        adivinhacao.selecao_nivel(values)
        view_jogo.read()


    elif event == '-BT_MEDIUM-':
        values = 2
        adivinhacao.selecao_nivel(values)

    elif event == '-BT_HARD-':
        values = 3
        adivinhacao.selecao_nivel(values)
    
    elif values == '-CHUTE-':
        print(values)
        chute = values

    elif event == sg.Input():
        adivinhacao.testa_numero()

