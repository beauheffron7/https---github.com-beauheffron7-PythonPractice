def find_s(arr):
    for inx,r in enumerate(arr):
        if r=='S':
            return inx 
        
def part1_solver(s,arr):
    count = 0
    for index in range(len(arr[:-1])):
        if index==0:
            arr[1]= arr[index+1][:s]+'|'+arr[index+1][s+1:]
        for x in range(len(arr[index])):
            if arr[index][x]=='|':
                if arr[index+1][x]=='^':
                    count+=1
                    arr[index+1]= arr[index+1][:x-1]+'|'+arr[index+1][x:]
                    arr[index+1]= arr[index+1][:x+1]+'|'+arr[index+1][x+2:]
                else:
                    arr[index+1]= arr[index+1][:x]+'|'+arr[index+1][x+1:]
    return count, arr



with open(r"C:\Users\Beau\Desktop\advent_d7_input.txt", 'r') as f:
    txt = f.readlines()

arr=[]
for line in txt:
    line=line.strip('\n')
    arr.append(line)

test_arr = [
'.......S.......',
'...............',
'.......^.......',
'...............',
'......^.^......',
'...............',
'.....^.^.^.....',
'...............',
'....^.^...^....',
'...............',
'...^.^...^.^...',
'...............',
'..^...^.....^..',
'...............',
'.^.^.^.^.^...^.',
'...............'
]




s = find_s(arr[0])
count,arr = part1_solver(s,arr)

for r in arr:
    print(r)

print(count)