import rubiksparse


r = 'r'
b = 'b'
g = 'g'
y = 'y'
w = 'w'
o = 'o'
cw = 1
ccw = 0

adjacency = {
    r: ((y, (1,2)), (g, (0,1)),(w, (1,0)),(b,(2,1))),
    w: ((r, (1,2)), (g, (1,2)),(o, (1,2)),(b,(1,2))),
    g: ((y, (2,1)), (o, (0,1)),(w, (2,1)),(r,(2,1))),
    o: ((y, (1,0)), (b, (0,1)),(w, (1,2)),(g,(2,1))),
    b: ((y, (0,1)), (r, (0,1)),(w, (0,1)),(o,(2,1))),
    y: ((o, (1,0)), (g, (1,0)),(r, (1,0)),(b,(1,0)))
    }


class cube(object):

    def __init__(self):
        self.faces= rubiksparse.parse()

    def rotate_adjacent(self, face, direction):

        def extract_bottom((key, (x, y))):  #pulls out the bottom row w/respect to face
            adj_matrix = self.faces[key]
            if x ==1:
                side = adj_matrix[:,y]
            if y ==1:
                side = adj_matrix[x,:]
            return side[:]

        adj = adjacency(face)[:]
        if direction == ccw:
            adj.reverse()


        sides = map(extract_bottom, adjacency(face))
        sides = sides[-1:]+sides[:-1]


        insert = zip(adj, sides)

        def insert_bottom(((key, (x,y)), side)):
            adj_matrix = self.faces[key]
            if x ==1:
                adj_matrix[:,y] = side
            if y ==1:
                adj_matrix[x,:] = side

        map(insert_bottom, insert)

    def matrix_rotate(self, matrix,direction):
        corners = [(0,0), (2,0), (2,2), (0,2)]
        sides = [(1,0), (2,1), (1,2), (0,1)]
        if direction == ccw:
            corners.reverse()
            sides.reverse()
        last= matrix[corners[-1]]
        for corner in corners:
            temp = matrix[corner]
            matrix[corner]= last
            last = temp

        temp = matrix[sides[-1]]
        for side in sides:
            temp = matrix[side]
            matrix[side]= last
            last = temp



    def rotate(self, face, direction):
        # first, rotate the array
        self.matrix_rotate(self.faces[face])

        # then, rotate all of the adjacent faces
        self.rotate_adjacent(face, direction)



    def get(self, face):
        return self.faces[face[:,:]]