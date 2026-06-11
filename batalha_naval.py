import random

LINHAS = 5
COLUNAS = 10
NUM_NAVIOS = 5


def criar_tabuleiro():
    return [[0] * COLUNAS for _ in range(LINHAS)]


def mostrar_tabuleiro(tab, nome, navios):
    print(f"\n--- {nome} | Navios restantes: {navios} ---")
    print("   ", end="")
    for c in range(COLUNAS):
        print(f"{c+1:2}", end=" ")
    print()
    for i, linha in enumerate(tab):
        print(f"{i+1:2} ", end="")
        for cel in linha:
            if cel == 0:
                print("  .", end=" ")
            else:
                print(f"  {cel}", end=" ")
        print()


def posicionar_computador(tab_oculto):
    colocados = 0
    while colocados < NUM_NAVIOS:
        l = random.randint(0, LINHAS - 1)
        c = random.randint(0, COLUNAS - 1)
        if tab_oculto[l][c] == 0:
            tab_oculto[l][c] = 1
            colocados += 1


def posicionar_jogador(tab_oculto):
    print("\nAgora posicione seus navios no tabuleiro.")
    print(f"Voce tem {NUM_NAVIOS} navios pra posicionar (cada um ocupa 1 casa).\n")
    i = 1
    while i <= NUM_NAVIOS:
        print(f"  Navio {i}/{NUM_NAVIOS}")
        l, c = pedir_coord("linha", "coluna")
        if tab_oculto[l][c] == 1:
            print("  Ja tem um navio ai, escolhe outra posicao.")
            continue
        tab_oculto[l][c] = 1
        print("  Navio posicionado!\n")
        i += 1


def pedir_coord(nome_l="linha", nome_c="coluna"):
    while True:
        try:
            l = int(input(f"  {nome_l.capitalize()} (1-{LINHAS}): ")) - 1
            c = int(input(f"  {nome_c.capitalize()} (1-{COLUNAS}): ")) - 1
            if 0 <= l < LINHAS and 0 <= c < COLUNAS:
                return l, c
            print(f"  Fora do tabuleiro! Linha de 1 a {LINHAS}, coluna de 1 a {COLUNAS}.")
        except ValueError:
            print("  Digita so numeros inteiros.")


def ataque_jogador(tab_oculto_pc, tab_vis_pc):
    print("\nSua vez de atacar!")
    while True:
        l, c = pedir_coord()
        if tab_vis_pc[l][c] in ("X", "O"):
            print("  Essa coordenada ja foi atacada, escolhe outra.")
            continue
        break

    if tab_oculto_pc[l][c] == 1:
        tab_vis_pc[l][c] = "X"
        return True
    else:
        tab_vis_pc[l][c] = "O"
        return False


def ataque_computador(tab_oculto_j, tab_vis_j):
    while True:
        l = random.randint(0, LINHAS - 1)
        c = random.randint(0, COLUNAS - 1)
        if tab_vis_j[l][c] not in ("X", "O"):
            break

    print(f"\nComputador atacou: linha {l+1}, coluna {c+1}")

    if tab_oculto_j[l][c] == 1:
        tab_vis_j[l][c] = "X"
        return True
    else:
        tab_vis_j[l][c] = "O"
        return False


def jogar():
    print("=" * 40)
    print("       BATALHA NAVAL")
    print("=" * 40)

    # tabuleiros ocultos (com os navios de verdade)
    tab_j = criar_tabuleiro()
    tab_pc = criar_tabuleiro()

    # tabuleiros de feedback (so mostra ataques)
    vis_j = criar_tabuleiro()
    vis_pc = criar_tabuleiro()

    posicionar_jogador(tab_j)
    posicionar_computador(tab_pc)

    navios_j = NUM_NAVIOS
    navios_pc = NUM_NAVIOS

    print("\nTudo certo! Veja o estado inicial dos tabuleiros:")
    mostrar_tabuleiro(vis_pc, "Tabuleiro do Computador", navios_pc)
    mostrar_tabuleiro(vis_j, "Tabuleiro do Jogador", navios_j)

    while navios_j > 0 and navios_pc > 0:
        # turno do jogador
        acertou = ataque_jogador(tab_pc, vis_pc)
        if acertou:
            navios_pc -= 1
            print(f"  ACERTOU um navio inimigo! Navios do computador restantes: {navios_pc}")
        else:
            print("  Errou, agua...")

        mostrar_tabuleiro(vis_pc, "Tabuleiro do Computador", navios_pc)
        mostrar_tabuleiro(vis_j, "Tabuleiro do Jogador", navios_j)

        if navios_pc == 0:
            break

        # turno do computador
        acertou = ataque_computador(tab_j, vis_j)
        if acertou:
            navios_j -= 1
            print(f"  O computador afundou um dos seus navios! Seus navios restantes: {navios_j}")
        else:
            print("  O computador errou!")

        mostrar_tabuleiro(vis_pc, "Tabuleiro do Computador", navios_pc)
        mostrar_tabuleiro(vis_j, "Tabuleiro do Jogador", navios_j)

    print("\n" + "=" * 40)
    if navios_pc == 0:
        print("Parabens! Voce afundou toda a frota inimiga!")
    else:
        print("O computador afundou todos os seus navios. Boa sorte na proxima!")
    print("\nObrigado por jogar!")
    print("Desenvolvido por: Eduardo Neves, Guilherme Miyadi Suguimati")
    print("=" * 40)


if __name__ == "__main__":
    jogar()
