from datetime import datetime
startTime = datetime.now()

global part1_counter
global part2_counter
part1_counter = 0
part2_counter = 0


def id_checker(start,end):
    global part1_counter,part2_counter

    while int(start)<=int(end):
        result = str(number_check(start))
        if result[0] == '1':
            part1_counter+=int(start)
        if result[1] == '1':
            part2_counter+=int(start)
        start=str(int(start)+1)


def number_check(num):
    x=''
    part1_pass = 0
    part2_pass = 0

    for digit in num:
        x+=str(digit)
        occurences = num.count(x)
        if x=='0':
            return '00'
        elif occurences==1:
            return str(part1_pass)+str(part2_pass)
        else:
            if occurences>2 and occurences*len(x) == len(num):
                part2_pass=1
            elif occurences==2 and occurences*len(x) == len(num):
                #invalid id
                return '11'
            
    return str(part1_pass)+str(part2_pass)
       


with open(r"C:\Users\Beau\Desktop\advent_d2_input.txt", 'r') as f:
    ids= f.readlines()
    for x in ids:
        list = x.replace('\n','').split(',')

test_list = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']

for pair in list:
    id = pair.split('-')
    id_checker(id[0],id[1])

print(f'Part 1:{part1_counter}, Part2: {part2_counter}, {datetime.now() - startTime} seconds')
