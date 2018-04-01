class Jogador:

    def __init__(self, nome, inventario):
        self.nome = nome
        self.inventario = inventario
        self.pontos = 0
        self.vitoria = False
        self.sala_atual = 'placeholder'
        self.item_equipado = None


    def ver_inventario(self, retorna_itens=False):
        if not retorna_itens:
            print("\nTotal de itens: {}".format(len(self.inventario)))
            print("Seus itens: \n")
        nome_dos_itens = []
        for item in self.inventario:
            if not retorna_itens:
                print(item['nome'])
            nome_dos_itens.append(item['nome'])

        if retorna_itens:
            return nome_dos_itens


    def __str__(self):
        print("Nome: {}".format(self.nome))
        print("Classe: {}".format(self.classe))
        print("Vida: {}".format(self.hp))
        print("Mana: {}".format(self.mp))
        print("Força: {}".format(self.forca))
        print("Pontos: {}".format(self.pontos))
