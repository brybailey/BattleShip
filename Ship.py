from random import randint

class Ship(object):

    ship_length = 0
    up_or_accross = 0
    ship_positions = []
    ship_head_x = 0
    ship_head_y = 0
    
    def __init__(self, board_size):
        #create a ship with random length and positioning
        self.ship_length = randint(1,  board_size - 1 )
        self.up_or_accross = randint(0,1)


        #Ship is horizontal
        if self.up_or_accross == 0:
            self.ship_head_y = randint(0, board_size-self.ship_length )
            self.ship_head_x = randint(0, board_size-1)
        #Ship is vertical
        else:
            self.ship_head_y = randint(0, board_size-1)
            self.ship_head_x = randint(0, board_size-self.ship_length )


            
#        self.ship_positions[self.ship_head_x][self.ship_head_y] = "1"
        self.ship_position()
        if not self.ship_positions:
            print self.ship_length
            print self.ship_head_x, self.ship_head_y

    def which_way(self):
        if self.vertical_or_horizontal() == 0:
            if self.ship_head_x + self.ship_length > 5:
                return 0
                
            
    """def vertical_or_horizontal(self):
        #ship is horizontal
        if self.up_or_accross == 0:
            return 0
        #ship is vertical
        elif self.up_or_accross == 1:
            return 1"""

    def length(self):
        return self.ship_length

    def ship_position( self ):
        for x in range(0, self.ship_length):
            if self.up_or_accross == 0:
                self.ship_positions.append( str(self.ship_head_y + x ) + "," + str (self.ship_head_x ) )
                #self.ship_positions[ self.ship_head_x ][ self.ship_head_y + x + 1 ] = str(x + 2)
            else:
                self.ship_positions.append( str( self.ship_head_y ) + ", " + str( self.ship_head_x + x ) )
                #self.ship_positions[ self.ship_head_x + x + 1 ][ self.ship_head_y ] = str(x + 2)
      
            

test_ship = Ship( 5 )
print test_ship.ship_positions

        
    
