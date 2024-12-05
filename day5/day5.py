import numpy as np
import re

import numpy as np

def check_rules(line,ruleslist):
    rules_set = set(map(tuple, ruleslist))
    for ic in range(len(line)):   
        for ic2 in range(ic+1,len(line)):   
            tmpR = (line[ic2], line[ic])
            if (tmpR in rules_set): return False; 
    return True
    
def part1(listpages,ruleslist):
    sum_centers=0;   
    for i in listpages: 
        if check_rules(i,ruleslist): sum_centers+=i[int(len(i)*0.5)]
    return sum_centers
    


def check_rules_swap(line, ruleslist):
    rules_set = set(map(tuple, ruleslist)) 
    tmp_line = np.array(line) 
    cnt = 0 
    print(line)
    while not check_rules(tmp_line, ruleslist):  
        cnt += 1
        swapped = False  # Flag to track if any swaps are made

        for i in range(len(tmp_line)):
            for j in range(i + 1, len(tmp_line)):
                tmp_rule = (tmp_line[j], tmp_line[i])
                if tmp_rule in rules_set:
                    new_arr=[]
                    
                    for inn in range(len(tmp_line)):
                        if inn<i: new_arr.append(tmp_line[inn])
                        if inn==i: new_arr.append(tmp_line[j]); new_arr.append(tmp_line[inn])
                        if inn>i and inn!=j: new_arr.append(tmp_line[inn])
                        
                    tmp_line=new_arr
                    swapped = True
                    print(f"Swapped: {tmp_line[i]} <--> {tmp_line[j]}, New Line: {tmp_line}")

        if not swapped: 
            break

        if cnt > 1000:  
            print("Failed to satisfy rules within 1000 iterations")
            return None

    return tmp_line


def fixed_order_centers(line,ruleslist):

    mex=0;
    new_line=check_rules_swap(line,ruleslist)
    mex=new_line[int(len(new_line)*0.5)]
    return mex


def part2(listpages,ruleslist):
    sum_centers=0;   
    cnt=0;
    for i in listpages: 
        cnt+=1;
        if not check_rules(i,ruleslist) :   
            sum_centers+= fixed_order_centers(i,ruleslist)
    
    return sum_centers

def main(filename):
    rules=[]
    pages=[]
    with open(filename,'r') as file:
        for i in file:
            if re.search(r'\|',i): rules.append(list(map(int,i.strip().split('|'))))
            if re.search(r'\,',i): pages.append(list(map(int,i.strip().split(','))))
                
    print(f"Part1: What do you get if you add up the middle page number from those correctly-ordered updates? \n", part1(pages,rules))
    print(f'Part2: What do you get if you add up the middle page numbers after correctly ordering just those updates?\n',part2(pages,rules))


if __name__ == "__main__":
    filename = '../puzzles/puzzle5.txt'  # Specify the filename here
    main(filename)

