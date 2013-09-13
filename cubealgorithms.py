#Implements overall design of solving algorithm
#Uses implementation of cube.rotate(face, direction)

def solve(self):
#Solves Rubik's cube
    self.start_cross()
    self.white_cross()
    self.bottom_layer()
    self.middle_layer()
    self.top_face()
    self.top_layer()




def start_cross(self):
    #Creates a yellow-centre white cross on top.
    #First step to solving algorithm


def white_cross(self):
#Creates a white cross on the bottom
    def white_cross_helper(self, face):
    #Aligns each side of the white cross
        top_rotations, = self.match_center(face)
        counter = 0
        while counter < top_rotations:
            self.top_rotate()
            counter += 1
        self.rotate(face, clockwise)
        self.rotate(face, clockwise)
    def match_center(self, face):
    #Returns the number of rotations needed to align middle pieces
    self.white_cross_helper(blue)
    self.white_cross_helepr(red)
    self.white_cross_helper(green)
    self.white_cross_helper(orange)
    
def bottom_layer(self):
#Solves the bottom layer
    def corner_matcher(self, color, dircetion):
    #Matches the certain corners pieces with the correct centre
    def corner_finish(self, face, direction):
    #Performs correct algorithm to add a bottom layer corner
        if color is green and direction is 'left':
            self.rotate(red, counterclockwise)
            self.rotate(yellow, counterclockwise)
            self.rotate(red, clockwise)
            self.rotate(yellow, clockwise)
            self.rotate(green, clockwise)
            self.rotate(yellow, clockwise)
            self.rotate(green, counterclockwise)
        #Repeat conditionals for each condition
    self.corner_matcher(blue, left)
    self.corner_finisher(blue, left)
    self.corner_matcher(blue, right)
    self.corner_finisher(blue, right)
    self.corner_matcher(green, left)
    self.corner_finisher(green, left)
    self.corner_matcher(green, right)
    self.corner_finisher(green, right)
    self.corner_matcher(red, left)
    self.corner_finisher(red, left)
    self.corner_matcher(red, right)
    self.corner_finisher(red, right)
    self.corner_matcher(green, left)
    self.corner_finisher(green, left)
    self.corner_matcher(green, right)
    self.corner_finisher(green, right)
   ######
   
def middle_layer(self):
#Solves the middle layer
    def set_top(self, color):
    #Rotates top layer to correct orientation for middle algorithm
    def middle_layer_for(self, color):
        #Performs the middle layer algorithm for a certain colour
        if color == green:
            self.rotate(green, counterclockwise)
            self.rotate(yellow, counterclocwise)
            self.rotate(green, clockwise)
            self.rotate(yellow, clockwise)
            self.rotate(orange, clockwise)
            self.rotate(yellow, clockwise)
            self.rotate(orange, counterclockwise)
        #Repeat code for other cases
    self.set_top(blue)
    self.middle_layer_for(blue)
    self.set_top(green)
    self.middle_layer_for(green)
    self.set_top(red)
    self.middle_layer_for(red)
    self.set_top(orange)
    self.middle_layer_for(orange)
    
def top_face(self):
#Solves the top face by
    def set_yellow_cross(self):
    #Identifies the current position of the yellow cross and aligns it
    #to perform the algorithm
    def check_top(self):
    #Returns whether or not the top is finished
        self.rotate(red, clockwise)
        self.rotate(yellow, clockwise)
        self.rotate(green, clockwise
    def top_algorithm(self):
    #Performs top algorithm
    while check_top is not true:
        self.set_yellow_cross()
        self.top_algorithm

def top_layer(self):
#Solves the final layer of the cube
    def set_back(self):
    #Rotates top layer to correct orientation for top layer algorithm
    def finishing_algorithm(self)
    #Performs algorithm to solve top layer 
    def finished(self)
    #Returns whether or not the cube is finished
    while not self.finished():
        self.set_back()
        self.finishing_algorithm

def match_center(self):
#Returns number of clockwise top rotations:


