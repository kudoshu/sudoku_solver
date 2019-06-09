import sys


def make_grid(data):
    temp = iter([int(i) if i.isdigit() else None for i in data])
    return [[next(temp) for i in range(9)] for i in range(9)]


def subgrid(grid, row, column):
    return [grid[3 * (row // 3) + (x // 3)][3 * (column // 3) + (x % 3)] for x in range(9)]


def is_unique(data):
    temp = [i for i in data if i is not None]
    return len(temp) == len(set(temp))


def verify(grid, row, column):
    # check subgrid,row,column
    return is_unique(subgrid(grid, row, column)) and is_unique(grid[row]) and is_unique([grid[x][column] for x in range(9)])


def print_grid(grid):
    for row in range(9):
        print(''.join([str(i) if i is not None else '.' for i in grid[row]]), end=' ')
    else:
        print()


def solve(grid, p):
    if p > 80:
        return True
    else:
        row = p // 9
        column = p % 9
        if grid[row][column] is not None:
            if solve(grid, p + 1):
                return True
        else:
            for v in range(1, 10):
                grid[row][column] = v
                if verify(grid, row, column):
                    if solve(grid, p + 1):
                        return True
            grid[row][column] = None
            return False


def main():
    arg = sys.argv

    if len(arg) == 1:
        data = input().replace(' ', '').strip()
    else:
        with open(arg[1]) as f:
            data = f.readline().replace(' ', '').strip()

    grid = make_grid(data)
    solve(grid, 0)
    print_grid(grid)


if __name__ == '__main__':
    main()
