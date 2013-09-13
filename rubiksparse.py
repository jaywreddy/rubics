
def createArray(index,main_array):
        return_array = []
        line_array = cube_list[index-4:index+5]
        count = index-4 # For counting the main array
        for x in range(0,3):
                return_array.append([])
                for j in range(0,3):
                        return_array[x].append(main_array[count])
                        count += 1
        return return_array


cube_text = open("cube.txt", 'r').read()
cube_list = cube_text.split(',')


# Init placeholder values for each side's face
yellow_face = 'y'
blue_face = 'b'
red_face = 'r'
green_face = 'g'
orange_face = 'o'
white_face = 'w'

char_index = 4

while char_index < 50:
	char_letter = cube_list[char_index]
	# Probably a better way for these if/elif's. Fix later
	if char_letter == 'y':
		yellow_face = createArray(char_index,cube_list)
	elif char_letter == 'b':
		blue_face = createArray(char_index,cube_list)
	elif char_letter == 'r':
		red_face = createArray(char_index,cube_list)
	elif char_letter == 'g':
		green_face = createArray(char_index, cube_list)
	elif char_letter == 'o':
		orange_face = createArray(char_index, cube_list)
	else:
		white_face = createArray(char_index, cube_list)
	char_index += 9

print("Yellow Face:", yellow_face, "Blue Face:", blue_face, "Red Face:", red_face, "Green Face:", green_face, "Orange Face:", orange_face, "White Face:", white_face)