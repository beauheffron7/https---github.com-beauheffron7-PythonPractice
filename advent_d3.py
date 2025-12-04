def largestcell(row):
    leadingdigit='0'
    followingdigit='0'

    for index,digit in enumerate(row):
        if int(digit)>int(leadingdigit) and index != len(row)-1:
            leadingdigit=str(digit)
            followingdigit='0'
        elif int(digit)>int(followingdigit):
            followingdigit=str(digit)
             

    part1_ans = int(leadingdigit+followingdigit)
    return part1_ans

def largestcellbreaks(row):
    remainingdigits=12
    part2_ans= []
    prev_index = -1
    while remainingdigits>0:
        highest_dig='0'
        highest_dig_index='0'
        for index,digit in enumerate(row):
            if index+remainingdigits<=len(row) and int(digit)>int(highest_dig) and index>prev_index:
                highest_dig_index = index
                highest_dig = digit

        part2_ans.append(highest_dig)
        prev_index = highest_dig_index
        remainingdigits-=1
    #print(part2_ans)
    return int("".join(part2_ans))
               



with open(r"C:\Users\Beau\Desktop\advent_d3_input.txt", 'r') as f:
        batteries = f.readlines()
joltage_part1=0
joltage_part2=0
sample = ['987654321111111','811111111111119','234234234234278','818181911112111']

for bank in batteries:
    result = largestcell(bank.strip())
    result2 = largestcellbreaks(bank.strip())
    #print(result,' ', result2)
    joltage_part1 +=result
    joltage_part2+=result2

print(f'part1:{joltage_part1}, part2:{joltage_part2}')
