
from collections import defaultdict
class Day11:

    def preprocess(self, path):
        file = open(path)
        text = file.read().splitlines()
        self.seats = text


    def get_neighbors(self, current, seats):
        row = current[0]
        col = current[1]
        rules = {
            'U': (row - 1, col),
            'DOWN': (row + 1, col),
            'L': (row, col - 1),
            'R': (row, col + 1),
            'DLU': (row - 1, col - 1),
            'DLD': (row + 1, col - 1),
            'DRU': (row - 1, col + 1),
            'DRD': (row + 1, col + 1)
        }
        valid_neighbors = []
        size_col = len(seats[0])
        size2 = len(seats)
        for rule in rules:
            row, col = rules[rule]
            if row == size2 or row < 0:
                continue
            elif col == size_col or col < 0:
                continue
            else:
                valid_neig = seats[row][col]
                valid_neighbors.append(valid_neig)

        return valid_neighbors

    def change(self, current, neighbors, seats):
        current = seats[current[0]][current[1]]

        if current == '.':
            return None
        #print("Neigbors = ", neighbors)
        if current == 'L':
            #print("current is L try to change to #")
            if neighbors.count('#') == 0:
            #    print("change to #")
                return '#'
        elif current == '#':
            #print("CUrrent is # try to change to L")
            if neighbors.count('#') >= 4:
             #   print("Change to L")
                return 'L'
       # print("None")

    def Part1_new_solutuion(self):
        seats = self.seats
        temp = []
        round = 0
        size_row = len(seats)
        size_col = len(seats[0])
        print("Row size = ", size_row)
        print("COl size = ", size_col)


        while True:
            string = ''
            for row, seat_line in enumerate(seats):
                string = seat_line
                #print("printlen = ", len(seat_line))
                for col, seat in enumerate(seat_line):
                    current_pos = (row, col)
                   # print("Current pos ", current_pos)
                    current_neig = self.get_neighbors(current_pos, seats)
                    change = self.change(current_pos, current_neig, seats)
                   # print("change = ", change)
                    if change:
                        string = string[:col] + change + string[col + 1:]
                temp.append(string)
                #print("String = ", string)
                #print()
            #print("temp = ", temp)
            if temp == seats:
                break
            else:
                seats = []
                seats = temp
                temp = []

        def count_occurences(char):
            total = 0
            for seat_ in seats:
                total += seat_.count(char)
            return total

        self.part1 = count_occurences('#')

    def Part2(self):


        def new_neigbors(current, seats):
            # check left and right
            current_row = current[0]
            current_col = current[1]
            blocked_left, blocked_right = False, False

            left = seats[current_row][current_col - 8:current_col]
            right = seats[current_row][current_col:current_col + 8]
            down = seats[][]

            # check up and down

            # check diagonal down left and up right

            # check diagonal up left and down right


            pass

        def new_change(current, neighbors):
            pass


        seats = self.seats.copy()
        temp = []

        while True:
            string = ''

            for row, seat_line in enumerate(seats):
                for col, seat in enumerate(seat_line):



        pass


path_ = "inputs\day11.txt"
day11 = Day11()
day11.preprocess(path_)

day11.Part1_new_solutuion()

print("Part1 = ", day11.part1)