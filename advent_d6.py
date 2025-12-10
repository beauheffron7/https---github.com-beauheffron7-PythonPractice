with open(r"C:\Users\Beau\Desktop\advent_d6_input.txt", 'r') as f:
    txt = f.readlines()
arr=[]
for line in txt:
    line=line.strip('\n')
    arr.append(line)

test_arr = [
'123 328  51 64 ',
' 45 64  387 23 ',
'  6 98  215 314',
'*   +   *   +  '
]

#part 1
num_arr = []
for line in arr:
    line_nums = []
    curr_num = ''
    for index,char in enumerate(line):
        if char.isdigit():
            curr_num+=char
            if len(line)==index+1:
                line_nums.append(int(curr_num))
                curr_num=''
        elif not char.isdigit() and curr_num.isdigit():
            line_nums.append(int(curr_num))
            curr_num=''
        elif char in ['+','*']:
            line_nums.append(char)
    num_arr.append(line_nums)
            
ans_arr = num_arr[0]
ops = num_arr[len(num_arr)-1]


for line in num_arr[1:-1]:
    for index,number in enumerate(line):
        if ops[index] == '*':
            ans_arr[index] = int(ans_arr[index]) * int(number)
        else:
            ans_arr[index] = int(ans_arr[index]) + int(number)

count = 0
for num in ans_arr:
    count+=num

print(f'Ans1: {count}')


#part 2

char_arr = []
for line in arr:
    line_chars = []
    for char in line:
        line_chars.append(char)
    char_arr.append(line_chars)

top=0
right=len(char_arr[:-1][0])-1

curr_num=''
a = []

while right>=0:
    if top == len(char_arr[:-1]):
        if char_arr[top][right] not in (' ','*','+'):
             curr_num+=char_arr[top][right]
        a.append(curr_num)
        top=-1
        right-=1
        curr_num=''
    elif char_arr[top][right].isdigit():
        curr_num+=char_arr[top][right]

    top+=1
#print(a)

ans2 = []
x=1
position =1
num=int(a[0])


#print(ops)


while position<len(a):
    if a[position]!= '' and ops[len(ops)-x] =='+':
        #print(num,int(a[position]))
        num=int(num) + int(a[position])
    elif a[position]!= '' and ops[len(ops)-x] =='*':
        #print(int(a[position]))
        num = int(num) * int(a[position])
    if position == len(a):
        ans2.append(num)
        x+=1
        num=a[position+1]
    if a[position] == '' and num!='':
        ans2.append(num)
        x+=1
        num=a[position+1]
        position+=1
        
    #print(a[position],num,x,ops[len(ops)-x])
    position+=1
ans2.append(num)

print('Ans2:',sum(ans2))










