import requests
import re
#session_token =

#headers = {'Cookie': f'session={session_token}'}
#url = 'https://adventofcode.com/2024/day/3/input'
#response = requests.get(url, headers=headers)
#input_data = response.text.strip()#.split('\n');

##MY FUNCTIONS
def mysum(x):
    return int(x[0])*int(x[1])
  
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

  
def part1(data):
    matches = re.findall(r"mul\((\d+),(\d+)\)",data)
    sum=0;
    for i in matches:
        sum+=mysum(i);
    return sum

def part2(data):
    matches = re.finditer(r"mul\((\d+),(\d+)\)", data)
    idont = [match.start() for match in  re.finditer(r"don't\(\)", data) ];
    ido = [match.start() for match in  re.finditer(r"do\(\)", data) ];

    check=True;
    index_allowed = []
    for imatch in range(len(data)):
        if imatch in idont:   check=False;
        if imatch in ido:     check=True;
        if check: index_allowed.append(imatch);
    totsum = 0;
    for match in matches:
        match_value = match.group(1,2)  # The full match string
        start_pos = match.start()   # Starting position of the match
        if start_pos in index_allowed:
            totsum += mysum( match_value)
    return totsum
def main(filename):
    """Main logic to read the matrix, extract diagonals, and count matches."""
    input_data = []
    with open(filename) as f:
        input_data = f.read()   
    print(f"Part 1: what do you get if you add up all of the results of the multiplications?", part1(input_data))
    print(f'Part 2: what do you get if you add up all of the results of just the enabled multiplications?',part2(input_data))


if __name__ == "__main__":
    filename = '../puzzles/puzzle3.txt'  # Specify the filename here
    main(filename)
