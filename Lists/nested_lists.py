nested_list = [[1,2,3],[3,4,5],[6,7,8]]

[[print(val) for val in values ] for values in nested_list]

board = [[number for number in range(1,4)] for val in range(1,4)] #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

tik_tak_toe_board = [["X" if number % 2 == 0 else "O" for number in range(0,3)] for val in range(0,3)]
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
