from api import Jogador, simulacao, plot
from pprint import pprint

if __name__ == "__main__":

    num_jogos = 1000

    player1 = Jogador(1)
    player2 = Jogador(2, reforco_vitoria=0, reforco_derrota=0)

    # player3 = Jogador(1, reforco_vitoria=0, reforco_derrota=0)
    # player4 = Jogador(2)

    playerA, playerB, vitoriasA, vitoriasB, empates = simulacao(
        player1,
        player2,
        num_jogos,
    )

    print()
    pprint(playerA.brain)
    print("---")
    pprint(playerB.brain)

    plot_name = "simulacao"
    plot(vitoriasA, vitoriasB, empates, plot_name, show=True)
