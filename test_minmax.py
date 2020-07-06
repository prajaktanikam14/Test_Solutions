'''
get_min = return minimum value from given input array
get_max = return maximun value from given input array

test_min = test function to check get_min function 
test_max = test function to check get_max function 
test_minmax= test function to check both function
'''

import array as arr

def get_min(input_arr ):
    min_val=input_arr [0]
    for i in range (len(input_arr )):
        if input_arr [i] < min_val:
            min_val=input_arr [i]
        
    return min_val

def get_max(input_arr ):
    max_val=input_arr [0]
    for i in range (len(input_arr )):
        if input_arr [i] > max_val:
            max_val=input_arr [i]
        
    return max_val

input_arr = arr.array('i', [111,2,33,5,66,1]) 

def test_min():
    assert get_min(input_arr) == 1
def test_max():
    assert get_max(input_arr) == 111
def test_minmax():
    assert get_min(input_arr) == 1
    assert get_max(input_arr) == 111

	
if __name__ == "__main__":
    test_min()
    test_max()
    test_minmax()
    print("Test passed")