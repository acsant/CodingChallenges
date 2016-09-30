import heapq;

# min heap holds the elements on the right half 
min_heap = [];
# max heap holds the elements on the left half
max_heap = [];
# top element is the median

def insert_heap (elem):
    # if both the heaps have nothing in them, insert at random
    if len(min_heap) == 0 and len(max_heap) == 0:
        heapq.heappush(min_heap, elem);
    # if the min heap has something in it, compare it to the content
    elif len(min_heap) != 0:
        if elem < min_heap[0]:
            heapq.heappush(max_heap, elem*-1);
        else:
            heapq.heappush(min_heap, elem);
    
    # post check to ensure balance between two heaps
    while len(min_heap) > len(max_heap) + 1:
        lowest = heapq.heappop(min_heap);
        heapq.heappush(max_heap, lowest*-1);
    
    while len(max_heap) > len(min_heap) + 1:
        # this number is negative
        highest = heapq.heappop(max_heap);
        # all elems in max heap are negative
        heapq.heappush(min_heap, highest*-1);
        
def get_median():
    # To get the median, if the sizes of both the heap are uneven,
    # return the top of the heap with the greater size
    if len(min_heap) > len(max_heap):
        return min_heap[0];
    elif len(max_heap) > len(min_heap):
        return max_heap[0]*-1;

    # if sizes are the same, average them out
    return float(float(min_heap[0]) - float(max_heap[0]))/2.0;

# calculates the running median
N = int(raw_input().strip());
for i in range(N):
    num = float(raw_input().strip());
    insert_heap(num);
    print ("%.1f" % get_median());