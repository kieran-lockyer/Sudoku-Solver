def sudoku(puzzle):
    rows = '012345678'
    cols = '012345678'


    def cross(A, B):
        return [a + b for a in A for b in B]


    cells = cross(rows, cols)
    unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('012', '345', '678') for cs in ('012', '345', '678')])
    units = dict((s, [u for u in unitlist if s in u]) for s in cells)
    peers = dict((s, set(sum(units[s], [])) - set([s])) for s in cells)
    links = {}
    for x in range(len(cells)):
        links[cells[x]] = (x // 9, x % 9)


    def needs(puzzle):
        total_needs = {}
        for cell in cells:
            coord1 = links[cell]
            if puzzle[coord1[0]][coord1[1]] == 0:
                options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for partner in peers[cell]:
                    coord2 = links[partner]
                    if puzzle[coord2[0]][coord2[1]] in options:
                        options.remove(puzzle[coord2[0]][coord2[1]])
                total_needs[cell] = options
        return total_needs


    def fill(puzzle, needs):
        for cell in cells:
            if cell in needs.keys():
                coord = links[cell]
                if len(needs[cell]) == 1:
                    puzzle[coord[0]][coord[1]] = needs[cell][0]
        return puzzle


    def solved(puzzle):
        for row in puzzle:
            if 0 in row:
                return False
        return True


    while True:
        fill_needs = needs(puzzle)
        puzzle = fill(puzzle, fill_needs)
        if solved(puzzle):
            return puzzle