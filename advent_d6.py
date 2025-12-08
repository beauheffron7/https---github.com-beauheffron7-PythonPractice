
test_arr = ['123 328  51 64 ',
' 45 64  387 23 ',
'  6 98  215 314',
'*   +   *   +  '
]

num_arr = []
for line in test_arr:
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
        print(number)
        if ops[index] == '*':
            ans_arr[index] = int(ans_arr[index]) * int(number)
        else:
            ans_arr[index] = int(ans_arr[index]) + int(number)

print(ans_arr)
