global zero_counter

def zero_solver(rotations, sp):
    global zero_counter
    zero_counter = 0
    for r in rotations:
        ep = calc(sp,r)
        sp=ep
    return zero_counter

def calc(sp,mvmt):
    global zero_counter
    m = int(mvmt[1:])%100
    if int(mvmt[1:])>100:
        zero_counter+=(int(mvmt[1:])-m)/100
    if(mvmt[0]=='L'):
        if sp-m<0:
            ep= 100 +(sp-m)
        else:
            ep= sp-m
        if sp<ep and sp!=0 and ep!=0:
            #part 2 answer removing double counting of start/endpoints
            zero_counter+=1
    else:
        if sp+m>99:
            ep= sp+m-100
        else:
            ep= sp+m
        if sp>ep and sp!=0 and ep!=0:
            #part 2 answer removing double counting of start/endpoints
            zero_counter+=1
    if ep ==0:
        #part 1 answer
        zero_counter+=1
    print(zero_counter,ep)
    return ep

test = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
start_point= 50

with open(r"C:\Users\Beau\Desktop\advent_d1_input.txt", 'r') as f:
        rotations= f.readlines()

print(zero_solver(rotations,start_point))