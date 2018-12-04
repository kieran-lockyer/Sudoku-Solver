from CellPeers import peers

def sudoku(puzzle):
    def needs(puzzle):
        total_needs = {}
        for cell in peers.keys():
            cellToCheck = puzzle[int(cell[0])][int(cell[1])]
            if cellToCheck == 0:
                options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for peer in peers[cell]:
                    peerCell = puzzle[int(peer[0])][int(peer[1])]
                    if peerCell in options:
                        options.remove(peerCell)
                total_needs[cell] = options
        return total_needs

    def solve(puzzle, needs):
        for cell in needs.keys():
            if len(needs[cell]) == 1:
                puzzle[int(cell[0])][int(cell[1])] = needs[cell][0]
                for peer in peers[cell]:
                    if peer in needs.keys():
                        if needs[cell][0] in needs[peer]:
                            needs[peer].remove(needs[cell][0])
                needs[cell].remove(needs[cell][0])
        return puzzle, needs

    def solved(puzzle):
        for row in puzzle:
            if 0 in row:
                return False
        return True
    
    #function begins here
    fill_needs = needs(puzzle)
    while not solved(puzzle):
        puzzle, fill_needs = solve(puzzle, fill_needs)
    return puzzle

test1 = [
    [9, 0, 8, 6, 0, 0, 2, 0, 7],
    [0, 6, 0, 0, 8, 3, 0, 4, 0],
    [0, 0, 5, 7, 0, 1, 6, 8, 0],
    [0, 0, 0, 0, 0, 0, 8, 5, 2],
    [3, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 7, 4, 0, 0, 0, 0, 0, 0],
    [0, 5, 1, 4, 0, 6, 3, 0, 0],
    [0, 9, 0, 1, 3, 0, 0, 2, 0],
    [2, 0, 3, 0, 0, 8, 1, 0, 5]
]

test2 = [
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

# for future tests
evilPuzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 7, 1, 0, 0, 0, 6, 0],
    [0, 0, 1, 0, 6, 2, 7, 0, 0],
    [0, 0, 5, 2, 0, 0, 0, 8, 0],
    [0, 7, 0, 6, 0, 4, 0, 5, 0],
    [0, 3, 0, 0, 0, 5, 9, 0, 0],
    [0, 0, 3, 9, 4, 0, 5, 0, 0],
    [0, 8, 0, 0, 0, 7, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for line in sudoku(test2):
    print(line)