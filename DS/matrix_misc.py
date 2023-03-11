# NOTE: This is not a template to solve matrix questions with. It is a list of potentially helpful functions.


# This function allows you to treat a matrix as a single, 1D list. It allows you to access the idx-th element
# of the list that would be made by concatenate all rows of the matrix in order, without having to build this
# list beforehand.
def get_val_by_idx(matrix, idx):
    len_row = len(matrix[0])
    i = idx // len_row
    j = idx % len_row
    return matrix[i][j]

mat = [[1,5,9],[10,11,13],[12,13,15]]

# get_val_by_idx usage
for i in range(9):
    print(get_val_by_idx(mat, i))

