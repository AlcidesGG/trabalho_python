from Classes.Videocassete import Videocassete

videocassete_loja = Videocassete('praça', 'Gourmet')
videocassete_loja.receber_avaliacao('Gui', 10)
videocassete_loja.receber_avaliacao('Lais', 8)
videocassete_loja.receber_avaliacao('Emy', 2)

def main():
    Videocassete.listar_videocassetes()

if __name__ == '__main__':
    main()