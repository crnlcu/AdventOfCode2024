import requests
import re
#session_token =

#headers = {'Cookie': f'session={session_token}'}
#url = 'https://adventofcode.com/2024/day/1/input'
#response = requests.get(url, headers=headers)
#input_data = response.text.strip().split('\n');
def part1(filename):
    col1=[];
    col2=[];
    with open(filename, 'r') as f:
        for line in f:
            x,y = list(map(int, line.strip().split()))
            col1.append(x)
            col2.append(y)
    #aa=[ "3   4", #"4   3",#"2   5",#"1   3",#"3   9",#"3   3"]
    sum=0;  
    A=sorted(col1)
    B=sorted(col2)

    for i,j in zip(A,B):
        sum+=abs(i-j)
    
    return sum

def part2(data):
   col1=[];
   col2=[];
   with open(filename, 'r') as f:
        for line in f:
            x,y = list(map(int, line.strip().split()))
            col1.append(x)
            col2.append(y)
   sum=0;  

   for i in col1:
       for j in col2:
           if i==j: sum+=i;
   return sum

def main(filename):
    print(f"Part 1: What is the total distance between your lists?", part1(filename))
    print(f'Part 2: What is their similarity score?',part2(filename))


if __name__ == "__main__":
    filename = '../puzzles/puzzle1.txt'  # Specify the filename here
    main(filename)
