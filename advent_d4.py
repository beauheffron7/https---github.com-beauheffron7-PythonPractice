def roll_checker(arr):
    count=0
    cords_to_replace = []
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if(arr[x][y]=='@'):
                if(paper_checker(arr,x,y,len(arr),len(arr[x]))<4):
                    cords_to_replace.append(f'{x},{y}')
                    count+=1
    return count, cords_to_replace

def paper_checker(array,x_cord,y_cord,col_length,row_length):
    adj_rolls = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if x_cord+i >=0 and x_cord+i<col_length:
                if y_cord+j >=0 and y_cord+j<row_length and [i,j]!=[0,0]:   
                    if array[x_cord+i][y_cord+j]=='@':
                        adj_rolls+=1
    return adj_rolls

test_array = [
['.','.','@','@','.','@','@','@','@','.'],
['@','@','@','.','@','.','@','.','@','@'],
['@','@','@','@','@','.','@','.','@','@'],
['@','.','@','@','@','@','.','.','@','.'],
['@','@','.','@','@','@','@','.','@','@'],
['.','@','@','@','@','@','@','@','.','@'],
['.','@','.','@','.','@','.','@','@','@'],
['@','.','@','@','@','.','@','@','@','@'],
['.','@','@','@','@','@','@','@','@','.'],
['@','.','@','.','@','@','@','.','@','.']]

with open(r"C:\Users\Beau\Desktop\advent_d4_input.txt", 'r') as f:
        txt = f.readlines()
        array=[]
        for line in txt:
            l = []
            for char in line.strip():
                l.append(char)
            array.append(l)

iterations = 0
part2_ans = 0
done = -1
count=0

while done !=0:
    #print(test_array)
    count,coordinates = roll_checker(array) #change input
    for loc in coordinates:
        array[int(loc.split(',')[0])][int(loc.split(',')[1])]='.' #change input
    if iterations == 0:
        part1_ans = count
        part2_ans += count
        done=1
    else:
        part2_ans+=count
        done=count
    if count>0:
        iterations+=1

print(f'part 1: {part1_ans} \npart2: {part2_ans} \niterations: {iterations}')
