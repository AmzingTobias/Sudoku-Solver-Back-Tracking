class SodukuSolver():
    def __init__(self, grid):
        self.soduku_grid = grid
        self.original_grid = str(grid)

    # Algorithms to check valid soduku
    # Using format (row, col)

    def check_repeating_number_row(self, attempted_number, index):
        for col in range(len(self.soduku_grid[0])):
            if self.soduku_grid[index[0]][col] == attempted_number and col != index[1]:
                return True # Value is repeated in row
        return False # Value is not repeated in row

    def check_repeating_number_col(self, attempted_number, index):
        for row in range(len(self.soduku_grid)):
            if self.soduku_grid[row][index[1]] == attempted_number and row != index[0]:
                return True # Value is repeated in col
        return False # Value is not repeated in col

    def check_repeating_number_in_box(self, attempted_number, index):
        box_row = index[0] // 3
        box_col = index[1] // 3
        for row in range(box_row * 3, box_row * 3 + 3):
            for col in range(box_col * 3, box_col * 3 + 3):
                if ([row, col]) != (index) and self.soduku_grid[row][col] == attempted_number:
                    return True
        return False

    def check_valid(self, attempted_number, index):
        if not self.check_repeating_number_row(attempted_number, index):
            if not self.check_repeating_number_col(attempted_number, index):
                if not self.check_repeating_number_in_box(attempted_number, index):
                    return True
        return False

    def find_empty(self):
        for row in range(len(self.soduku_grid)):
            for col in range(len(self.soduku_grid[0])):
                if self.soduku_grid[row][col] == 0:
                    return (row, col)
        return None

    def solve(self):
        find = self.find_empty()
        if not find: #If not none
            return True
        else:
            row, col = find
        
        for possible_values in range(9):
            possible_values += 1
            if self.check_valid(possible_values, (row, col)):
                self.soduku_grid[row][col] = possible_values

                if self.solve():
                    return True
                self.soduku_grid[row][col] = 0
        return False

    def print_board(self):
        for row in range(len(self.soduku_grid)):

            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - - ")

            for col in range(len(self.soduku_grid[0])):

                if col % 3 == 0 and col != 0:
                    print(" | ", end="")
                
                if col == 8:
                    print(self.soduku_grid[row][col])
                else:
                    print(f"{str(self.soduku_grid[row][col])} ", end="")

if __name__ == "__main__":
    soduku_grid =  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solver = SodukuSolver(soduku_grid)
    print(solver.check_repeating_number_in_box(2, [2, 4]))
    solver.solve()
    solver.print_board()
    if str(solver.original_grid) == str(solver.soduku_grid):
        print("No Solutions")
    else:
        print("Solved")