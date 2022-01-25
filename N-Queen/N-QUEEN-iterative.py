import time
class Board:
    def __init__(self, size):
        self.N = size
        self.queens = [] # list of columns, where the index represents the row
        self.loopTime = 0
    
    def is_queen_safe(self, row, col):
        for r, c in enumerate(self.queens):
            self.loopTime+=1
            if r == row or c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def print_the_board(self):
        print ("solution:")
        for row in range(self.N):
            line = ['0 '] * self.N
            if row < len(self.queens):
                line[self.queens[row]] = '1 '
            print(''.join(line))

    def solution(self):
        self.queens = []
        col = row = 0
        sol = 0
        while True:
            while col < self.N and not self.is_queen_safe(row, col):
                col += 1
            if col < self.N:
                self.queens.append(col)
                if row + 1 >= self.N:
                    sol+=1
                    self.print_the_board()
                    self.queens.pop()
                    col = self.N
                else:
                    row += 1
                    col = 0
            if col >= self.N:
                # not possible to place a queen in this row anymore
                if row == 0:
                    print(f'Number of solution: {sol}')
                    return # all combinations were tried
                col = self.queens.pop() + 1
                row -= 1
        
q = Board(int(input('Enter: ')))
start_time = time.time()
q.solution()
print("--- %s seconds ---" % (time.time() - start_time))