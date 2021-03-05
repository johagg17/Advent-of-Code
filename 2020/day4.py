import regex as rx

valid_passports = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

# cid is optional
#one = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
#a = valid_passports.difference(one)

#di = {'byr': 1937, 'pid': 860033327}
#b = set(di)

#print(a)

# Om a har samma längds
# ^ in regex means the start of the string (appearing at the start of the string), $ means end of the string
# \d means single digit
# ? means optional
rkeys = {
    'byr': '^19[2-9][0-9]|200[0-2]$',
    'iyr': '^201[0-9]|2020$',
    'eyr': '^202[0-9]|2030$',
    'hgt': '^(?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in$',
    'hcl': '^#[0-9,a-f]{6}$',
    'ecl': '^amb|blu|brn|gry|grn|hzl|oth$',
    'pid': '^\d{9}$'
}
def preprocessing(path):
    with open(path, 'r') as file:
        lines = file.read().split('\n\n')
        file.close()
        return lines


def part1(dict_):
    set_d = set(dict_)
    new_set = valid_passports.difference(set_d)

    if len(new_set) == 0:
        del dict_['cid']
        valid = part2(dict_)
        return valid
    elif len(new_set) == 1 and 'cid' in new_set:
        valid = part2(dict_)
        return valid
    else:
        return 0

def part2(dict_): # If we access this function, all pass attributes are given

    value_count = 0
    for key in dict_:
        if rx.match(rkeys[key], dict_[key]):
            value_count += 1
    return value_count == len(dict_)

path = "inputs\day4.txt"
pass_ports = preprocessing(path)
passport_Dict = {}
valid = 0
part2_ = 0
for passP in pass_ports:
    passport_Dict = {}
    for x in passP.replace('\n', ' ').split(' '):
        xx = x.split(':')
        if xx[0] != '':
            key, value = xx[0], xx[1]
            passport_Dict[key] = value
    valid += part1(passport_Dict)

print("Valid pass =", valid)