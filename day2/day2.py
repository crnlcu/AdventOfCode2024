import requests
import re
#session_token =

#headers = {'Cookie': f'session={session_token}'}
#url = 'https://adventofcode.com/2024/day/2/input'
#response = requests.get(url, headers=headers)
#input_data = response.text.strip().split('\n');
def trend(line):
    delta_sign=None;
    for i in range(1,len(line)):
        delta=line[i]-line[i-1];
        if  abs(delta) > 3 or delta == 0: 
            return False
        if delta_sign is None:
            delta_sign = delta // abs(delta)  # Set initial sign
        elif delta // abs(delta) != delta_sign:
            return False  # If the direction changes, it's invalid
    return True

def new_trend(line):
    if trend(line):
        return True

    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]
        if trend(modified_line):
            return True

    return False

def part1(data):
    cnt=0;
    for line in data:
        if trend(line): cnt+=1;
    return cnt

def part2(data):
    cnt=0;
    for myline in data:
        vla=new_trend(myline)
        if vla: cnt+=1; 

    return cnt

def main(filename):
    input_data = []
    
    with open(filename, 'r') as f:
        for line in f:
            x = list(map(int, line.split()))
            input_data.append(x)
    print(f"Part 1: how many reports are safe?", part1(input_data))
    print(f'Part 2: single mutation in unsafe reports. How many reports are now safe?',part2(input_data))


if __name__ == "__main__":
    filename = '../puzzles/puzzle2.txt'  # Specify the filename here
    main(filename)
