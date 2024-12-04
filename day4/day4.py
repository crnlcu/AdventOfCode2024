import requests
import re
#session_token =

#headers = {'Cookie': f'session={session_token}'}
#url = 'https://adventofcode.com/2024/day/4/input'
#response = requests.get(url, headers=headers)
#input_data = response.text.strip().split('\n');

##MY FUNCTIONS
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def orizontal_matches(line,counter):
    xmas_m=re.findall(r"XMAS",line)
    counter+=len(xmas_m)
    samx_m=re.findall(r"SAMX",line)
    counter+=len(samx_m)
    return counter

def diagonali_of4(matrix4):
    rows=len(matrix4); #assumo che la matrice sia 4xN perche noi cerchiamo XMAS or SAMX
    cols=len(matrix4[0]);
    diagonals = []  
    for icol in range(cols):
        tmp_diagonal=[]
        tmp_diagonal_inverse=[]
        
        for irow in range(rows):

           # diagonale left-right top bottom
            if icol < cols - rows +1 : # 0,1,2...6 leggo solo vsdx
                tmp_diagonal.append(matrix4[irow][irow+icol])      
            if icol >= rows -1 : 
                tmp_diagonal_inverse.append(matrix4[irow][icol-irow]) 
       
        if icol < cols - rows +1 : 
            tmp_diagonal="".join(tmp_diagonal)
            diagonals.append(tmp_diagonal)
        if icol >= rows -1 :
            tmp_diagonal_inverse="".join(tmp_diagonal_inverse)
            diagonals.append(tmp_diagonal_inverse)
 
    return diagonals

def part1(data):
    counter=0;
    for line in data:
        counter=orizontal_matches(line,counter)

    transposed = [''.join(row) for row in zip(*data)]
    for line in transposed:
        counter=orizontal_matches(line,counter)

    rows=len(data)
    for irow in range(rows-4+1):
        new_sub=diagonali_of4(data[irow:irow+4])
        for line in new_sub:
            counter=orizontal_matches(line,counter)

    return counter


##MY FUNCTIONS FOR PART 2 looking for MAS-SAM in a X shape

def orizontal_matches_check(line):
    return bool(re.search(r"MAS|SAM", line))

def diagonali_of3(mymatrix):
    rows=len(mymatrix); #assumo che la matrice sia 4xN perche noi cerchiamo XMAS or SAMX
    cols=len(mymatrix[0]);
    Xmas = []  
    irow=1
    counter=0;
    for icol in range(1,cols-1):
        
        LR_diag = []
        RL_diag = []
        LR_diag.append(mymatrix[irow-1][icol-1])
        LR_diag.append(mymatrix[irow][icol])
        LR_diag.append(mymatrix[irow+1][icol+1])
        LR_diag="".join(LR_diag)

        if orizontal_matches_check(LR_diag): 
            RL_diag.append(mymatrix[irow-1][icol+1])
            RL_diag.append(mymatrix[irow][icol])
            RL_diag.append(mymatrix[irow+1][icol-1])
            RL_diag="".join(RL_diag)
            if orizontal_matches_check(RL_diag) : 
                counter+=1;
    return counter

def part2(input_data):
    rows=len(input_data)
    XMAS_counter=0;
    for irow in range(rows+1-3):
        XMAS_counter+=diagonali_of3(input_data[irow:irow+3])
    
    return XMAS_counter

def main(filename):
    """Main logic to read the matrix, extract diagonals, and count matches."""
    input_data = read_matrix_from_file(filename)
    
    print(f"Part 1: How many times does XMAS appear?", part1(input_data))
    print(f'Part 2: How many times does an X-MAS appear?',part2(input_data))


if __name__ == "__main__":
    filename = '../puzzles/puzzle4.txt'  # Specify the filename here
    main(filename)
