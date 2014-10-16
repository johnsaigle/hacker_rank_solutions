from collections import Counter

def gen_neighbors (x,y):
	global size
	X = Y = size
	return lambda x, y : [[x2, y2] for x2 in range(x-1, x+2)
    	                           for y2 in range(y-1, y+2)
        	                       if (-1 < x < X and
            	                       -1 < y < Y and
                	                   (x != x2 or y != y2) and
                    	               (0 <= x2 < X) and
                        	           (0 <= y2 < Y)) and
        	                       		abs(x2-x) != abs(y2-y)]

def read_in_array():
	rows = []
	with open('inputfile', 'r') as f:
		for line in f:
			rows.append(map(int, (str.split(line))))
	return rows

def find_sink(row,col, altitude_matrix):
	"""Recursively find the sink (ultimate drain point) for a cell"""
	neighbours = gen_neighbors(row, col)
	cell_neighbours = neighbours(row, col)
	neighbour_ranks = []
	for n in cell_neighbours:
		neighbour_ranks.append(altitude_matrix[n[0]][n[1]])
	cell_rank = altitude_matrix[row][col]
	sink_rank = min(neighbour_ranks)
	sink_index = neighbour_ranks.index(sink_rank)
	sink_coordinates = cell_neighbours[sink_index]

	if cell_rank > sink_rank:
		return(find_sink(sink_coordinates[0], sink_coordinates[1], altitude_matrix))
	else:
		return ((row, col))


def main():
	altitude_matrix = read_in_array()
	global size
	size = len(altitude_matrix)
	# recursively search throough the neighbour of every cell to find the sink
	# all cells with the same sink are in the same basin
	sink_list = []
	for row in xrange(size):
		for col in xrange(size):
			sink_list.append(find_sink(row, col, altitude_matrix))
	basins = Counter(sink_list)
	print("Basins, in format {(sinkx, sinky): size}: ")
	print(basins)

if __name__ == '__main__':
	main()