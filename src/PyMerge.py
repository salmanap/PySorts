'''
Created on Oct 20, 2010

@author: salman
'''

def merge_sort(array):
    merge_sort_r(0, len(array)-1, array)
    
def merge_sort_r(start, end, array):
    if start >= end:
        return
    middle = (start+end)/2
    merge_sort_r(start, middle, array)
    merge_sort_r(middle+1, end, array)
    merge(start, middle+1, end, array)

    
def merge(left, right, end, array):
    while (left < right and right <= end):
        if array[left] >= array[right]:
            swap_and_shift(right, left, array)
            left+=1
            right+=1
        else:
            left+=1
            
def swap_and_shift(from_pos, to_pos, array):
        holder = array[from_pos]
        #shifting the array by one
        shift_range = range(to_pos+1, from_pos+1)
        shift_range.reverse()
        for i in shift_range:
            array[i] = array[i-1]
        array[to_pos] = holder

if __name__ == "__main__":
    print 'Let\'s merge sort this array [1,9,5,7,4,6,10,3,2,8]'
    array = [1,9,5,7,4,6,10,3,2,8]
    merge_sort(array)
    print array