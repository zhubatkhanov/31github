"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

"""



# my solution (78ms, 14.41mb) -> (93.38%, 28.84%)
# def countNegatives(grid):
#     count = 0
#     for lst in grid:
#         if lst[len(lst) - 1] > 0:
#             continue
#
#         for item in lst[::-1]:
#             if item >= 0:
#                 break
#             count += 1
#
#     return count


# optimize solution in youtube
def countNegatives( grid):

    row_len = len(grid[0])
    col_len = len(grid)

    i = 0
    j = row_len - 1

    total = 0

    while i < col_len and j >= 0:
        if grid[i][j] < 0:
            total += col_len - i
            j -= 1
        else:

            i += 1

    return total


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))