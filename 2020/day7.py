from collections import defaultdict

class Day7():
    def __init__(self, path_):
        self.path = path_
        self.bags = defaultdict(dict)
    def preprocess(self):
        file = open(self.path)

        for bag in file:
            line = bag.replace('\n', '').replace('.', '')
            parent = line[:line.index('bags') - 1]
            childs = list(line[line.index('contain '):].replace('contain ', '').replace(', ', ':').split(':'))
            new_childs = []
            for child in childs:
                digit = child[0]
                if digit == '1':
                    replace_ = 'bag'
                else:
                    replace_ = 'bags'
                child = child.replace(replace_, '').replace(digit, '')
                child = child[child.index(' ') + 1:-1]
                if 'other' != child:
                    child_ = dict(number=digit, child=child)
                    new_childs.append(child_)
            if new_childs != []:
                self.bags[parent] = new_childs

    def IsShinyGold(self, child):
        if 'shiny gold' in child:
            return 1
        else:
            return 0

    def Part2(self, search):
        self.total = 0
        def recursive_child(bags, parent, visited, previous_numbers):
            if not isinstance(parent, str):
                parent = parent['child']

            for child in bags[parent]:
                if child not in visited:
                    print(child)
                    num = int(child['number'])
                    previous_numbers.append(num)
                    print("Prev num = ", previous_numbers)
                    self.total += sum(previous_numbers)

                    visited.append(child)
                    recursive_child(bags, child, visited, previous_numbers)

        visited = []
        previous = []
        for bag in self.bags:
            if bag not in visited:
                visited.append(visited)
                recursive_child(self.bags.copy(), bag, visited, previous)


    def Part1(self, search_node):
        self.contains_gold = 0
        '''
            Itterera inom alla parent, contains(shiny gold) ? Yes-> lägg till i visitedparent
            Leta sedan med hjälp av visited för att kolla dessa. 
        
        :return: 
        '''
        def search(bags, looking_for):
            front = [looking_for]
            visited = []
            parents = []
            while front!= []:
                current_ = front.pop(0)
                for bag in bags:
                    if current_ in bags[bag] and bag not in parents:

                        parents.append(bag)
                        front.append(bag)

            return len(parents)
        self.contains_gold = search(self.bags, search_node)



day7 = Day7("inputs\estday7.txt")
day7.preprocess()
#day7.Part1('shiny gold')
day7.Part2('shiny gold')
#print("Part1 = ", day7.contains_gold)
print("Part2 = ", day7.total)
