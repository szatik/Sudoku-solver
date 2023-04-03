import tkinter as tk

class SudokuGrid:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        # Create a 9x9 grid of Entry widgets
        self.entries = [[0 for x in range(9)] for y in range(9)]
        for i in range(9):
            for j in range(9):
                
                self.entries[i][j] = tk.Entry(master, width=1, font=('Arial', 16), border=2, justify="center")
                self.entries[i][j].grid(row=i, column=j, padx=2, pady=2)
                self.entries[i][j].insert(0, "0")
                self.entries[i][j].bind("<Button-1>", self.clear_entry)

                if i in (3,4,5) and j in (0,1,2,6,7,8):
                    self.entries[i][j].config(bg='gray')
                if j in (3,4,5) and i in (0,1,2,6,7,8):
                    self.entries[i][j].config(bg='gray')


        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=10 , column=0, columnspan=9)


        self.button2 = tk.Button(self.button_frame, text='Solve', command=self.solve)
        self.button2.grid(row=0, column=0)

        self.button2 = tk.Button(self.button_frame, text='Clear', command=self.clear_all)
        self.button2.grid(row=0, column=2)

        self.button2 = tk.Button(self.button_frame, text='Fill with sample', command=self.fill_sample_data)
        self.button2.grid(row=0, column=4)

    def clear_entry(self, event):
        event.widget.delete(0, tk.END)

    def clear_all(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, "0")
                self.entries[i][j].config(fg='black')
    
    def fill_sample_data(self):
        sample_data = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(sample_data[i][j]))
                self.entries[i][j].config(fg='black')

    def get_data(self):
        data = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(int(self.entries[i][j].get()))
            data.append(row)
 
    def solve(self):
        data = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = self.entries[i][j]
                value = entry.get()
                if value == "":
                    value = "0"
                if value != "0":
                    entry.config(fg='red')
                row.append(int(value))
            data.append(row)
        solution = self.solve_sudoku(data)
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(solution[i][j]))


    def solve_sudoku(self, puzzle):
        def find_empty(puzzle):
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j] == 0:
                        return (i, j)
            return None
        
        def is_valid(puzzle, row, col, num):
            for i in range(9):
                if puzzle [row][i] == num:
                    return False
            
            for i in range(9):
                if puzzle [i][col] == num:
                    return False

            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if puzzle[box_row+i][box_col+j] == num:
                        return False
            return True
        
        def solve_helper(puzzle):
            empty_cell = find_empty(puzzle)
            if not empty_cell:
                return True
            row, col = empty_cell
            for num in range(1, 10):
                if is_valid(puzzle, row, col, num):
                    puzzle[row][col] = num
                    if solve_helper(puzzle):
                        return True
                    puzzle[row][col] = 0
            return False

    # Make a copy of the original puzzle to avoid modifying it
        puzzle_copy = [[puzzle[i][j] for j in range(9)] for i in range(9)]
        solve_helper(puzzle_copy)
        return puzzle_copy


root = tk.Tk()
sudoku = SudokuGrid(root)
root.mainloop()