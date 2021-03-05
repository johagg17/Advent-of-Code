'''
    Airplane use binary space partitioning to seat people
    a seat could be specified as FBFBBFFRLR where F means front, B means back
    L means left and R means right

    First chars will always be F or B, they are used to identify the rows on the airplane (128 different rows)
    (0 - 127) rows.

    Each letter tels which halft of a region the given seat is in.
    If we would try to decode FBFBBFFRLR we would get:
    F - front - (128/2) = 64 -> (0 - 63)
    B - Back - 64/2 = 32 -> (32 - 63)
    F - front - 32/2 = 16 -> (32 - 47)
    B - Back - 16/2 = 8 -> (40 - 47)
    B - Back - 8/2 = 4 -> (44 - 47)
    F - Front 4/2 = 2 -> (44 - 45)
    F - Front 2/2 = 1 -> (44) which is the row for our seat

    The chars left to analyze is RLR. columns 0 - 7
    Right means upper half and left means lower half
    R -> Right - 8/2 = 4 -> (4 - 7)
    L -> Left - 4/2 = 2 -> (4 - 5)
    R -> Right - 2/2 -> (5)
    as final we get column 5

    Our seat is placed at row 44 column 5. The seatID is computed through row*8 + column
    seatID for above example = 44*8 + 5 = 357

    For our problem, what is the highest seatID in our list of boarding passes ?

'''
pass_ = {
    'F': 0,
    'B': 1,
    'R': 2,
    'L': 3
}

class Day5(object):
    def __init__(self, path):
        self.file = path
        self.list = []
        self.seats = []
        self.seatIDs = set()

    def preprocessing(self):
        file = open(self.file)
        self.list = text = file.read().splitlines()

    def analyze_Bpass(self, boarding_pass):
        analyze_row = boarding_pass[:-3]
        analyze_col = boarding_pass[7:]
        limits = [0, 127]
        row, col = None, None
        #print("Boarding pass = ", boarding_pass)
        for char in analyze_row:
            value = pass_[char]
            if value == 0:
                difference = limits[1] - limits[0]
                new_value = int(difference / 2)
                limits[1] -= new_value
                limits[1] -= 1
            elif value == 1:
                difference = limits[1] - limits[0]
                new_value = int(difference / 2)
                limits[0] += new_value
                limits[0] += 1
        row = limits[0]
        limits = [0, 7]
        for char in analyze_col:
            value = pass_[char]
            if value == 2:
                difference = limits[1] - limits[0]
                new_value = int(difference / 2)
                limits[0] += new_value
                limits[0] += 1
            elif value == 3:
                difference = limits[1] - limits[0]
                new_value = int(difference / 2)
                limits[1] -= new_value
                limits[1] -= 1

        col = limits[0]
        seatID = (row*8) + col
        self.seatIDs.add(seatID)
        seat = {'row': row, 'col': col, 'seatID': seatID}
        self.seats.append(seat)
        return seatID

    def part1(self):
        highest_id = 0
        for boarding_pass in self.list:
            seatID = self.analyze_Bpass(boarding_pass)
            if seatID > highest_id:
                highest_id = seatID
        self.highest_id = highest_id
        return highest_id


    def part2(self):
        high = self.highest_id
        seatIDs = self.seatIDs
        for id in range(0 , high):
           if (id not in seatIDs and ((id + 1) in seatIDs and (id - 1) in seatIDs)):
               return id


day5 = Day5("inputs\day5.txt")
day5.preprocessing()
part1_ = day5.part1()
part2_ = day5.part2()

print("Part1 = ", part1_)
print("Part2 = ", part2_)