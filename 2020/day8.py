
class Day8():
    def __init__(self, path_):
        self.instructions = []
        self.visited = set()
        self.index = 0
        self.acc = 0
        self.path = path_

    def preproccess(self):
        file = open(self.path)
        self.instructions = []
        for text in file.readlines():
            self.instructions.append(text.splitlines()[0])

    def decode_instruction(self, instruction, index, visited):
        instruct, value = instruction[0], instruction[1]
        value = int(value)
        acc_val = 0
        if index not in self.visited:
            self.visited.add(index)
            if instruct == 'jmp':
                index = index + value
            elif instruct == 'acc':
                acc_val = value
                index += 1
            elif instruct == 'nop':
                index += 1
            return index, acc_val
        else:
            return 0, acc_val
    def clear_mem(self):
        self.index = 0
        self.visited = set()
        self.acc = 0
        self.preproccess()

    def Part1(self):
        while True:
            if self.index == len(self.instructions):
                return 0
            elif self.index in self.visited:
                return -1

            current = self.instructions[self.index].split(' ')
            self.index, acc_ = self.decode_instruction(current, self.index, self.visited)
            self.acc += acc_


    def Part2(self):
        op_index = 0
        op1 = 'jmp'
        op2 = 'nop'
        while self.Part1() != 0:
            self.clear_mem()
            list_op = []
            for i, op in enumerate(self.instructions):
                if (op1 in op or op2 in op):
                    list_op.append((i, op))
            index, op = list_op[op_index]
            if op1 in op:
                self.instructions[index] = self.instructions[index].replace(op.split(" ")[0], op2)
            elif op2 in op:
                self.instructions[index] = self.instructions[index].replace(op.split(" ")[0], op1)
            op_index += 1


path = "inputs\day8.txt"
day8 = Day8(path)
day8.preproccess()
day8.Part1()
print("Part1 = ", day8.acc)
day8.Part2()
print("Part2 = ", day8.acc)
