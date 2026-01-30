# write your solution here

def row_sums() -> list:
    list_of_sums = []
    with open('matrix.txt') as file:
        for line in file:
            line = line.replace('\n','')
            
            sum_of_row = 0
            parts = line.split(',')
            for number in parts:
                sum_of_row += int(number)
            list_of_sums.append(sum_of_row)
    return(list_of_sums)
       
def matrix_sum() -> int:   
    list_of_sums = row_sums()
    return sum(list_of_sums)

def matrix_max() -> int:   
    largest = 0
    with open('matrix.txt') as file:
        for line in file:
            line = line.replace('\n','')
            
            parts = line.split(',')
            for number in parts:
                if number > largest:
                    largest = int(number)

    return largest

if __name__ == "__main__": 
    print(matrix_max())