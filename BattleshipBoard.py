from Ship import Ship

class BattleshipBoard(object):


    ship_row = 0
    ship_col = 0
    board = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    
    def __init__(self, num_ships, board_size):
        #initialize variables
        """self.ship_row = ship_row
        self.ship_col = ship_col
        self.board = board """
        self.num_ships = num_ships
        self.board_size = board_size
        
        #create a board of size specified by input
        for x in range(board_size):
            self.board.append(["O"] * 5 )

    def print_board(self):
        for row in self.board:
            print " ".join(row)

    def board_length(self):
        return self.board_size

    def pos_empty(shipx, shipy):
        return board[shipx][shipy] == 'O'

    def can_place_ship(ship):
        for x in ship.ship_positions:
            if x != "0":
                return "NO"
            else: return "YES"

test_board = BattleshipBoard(3, 5)
#test_board.print_board()
test_ship = Ship( test_board.board_length() )
#print test_board.get_length()



        
