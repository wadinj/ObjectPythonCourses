class Board:
    
    # Le constructeur permet d'initialiser votre classe en une instance
    # L'appel de ce constructeur est une fonction comme toute les autres, elle peut prendre en arguments des paramètres
    # Le mot-clé "self", permet de signifier que la fonction doit-être appelée sur une instance de notre classe.
    # Self permet aussi de référencer un attribut.
    def __init__(self):
        print('Hello Board')
        self.attribut_du_board = 'plateau'

    # Le mot-clé self, signifie encore une fois qu'une instance est obligatoire
    def uneMethode(self):
        print('Une methode est une fonction qui doit être appelée à partir d\'une instance de la classe')

    @staticmethod
    def uneMethodeStatic():
        print('Cette méthode peut-être appelée sans instance')

    # Fonction prédéfini qui surchage le print de cet objet
    def __repr__(self):
        return 'Un beau plateau !'
        
board = Board()
print(board.attribut_du_board)

Board.uneMethodeStatic()
print(board)