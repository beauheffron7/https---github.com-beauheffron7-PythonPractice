
def fresh(id,arr):
    for range in arr:
        start = int(range.split('-')[0])
        end = int(range.split('-')[1])
        if id >=start and id <=end:
            return 1 #'fresh'
    return 0 #'spoiled'

def all_fresh_ingredients(arr):
    count=0
    #order
    arr = sorted(arr, key = lambda item: int(item.split('-')[0]))
    #remove overlap
    start_before = 0
    end_before = 0
    for item in arr:
        start = int(item.split('-')[0])
        end = int(item.split('-')[1])
        if start<=end_before and end_before<=end:
            start = end_before+1
            ########## HERE ######################
        elif :
        ##########################################
        start_before=start
        end_before=end
        count+=end-start+1

    return count



with open(r"C:\Users\Beau\Desktop\advent_d5_input.txt", 'r') as f:
    txt = f.readlines()

    id_ranges=[]
    ids = []

    for line in txt:
        line=line.strip('\n')
        if line=='' or line=='\n':
            pass
        elif '-' in line:
            id_ranges.append(line)
        else:
            ids.append(int(line))

test_ranges = ['3-5',
'10-14',
'16-20',
'12-18']

test_ids = [
1,
5,
8,
11,
17,
32]


fresh_count =0

for id in ids:
    fresh_count+=fresh(id,id_ranges)

id_count = all_fresh_ingredients(id_ranges)


print(f'Ans 1: {fresh_count}, Ans 2: {id_count}')