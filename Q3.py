import random

randomList = random.sample(xrange(1, 501),500)
nth = 166
#list = sorted(list)
print (randomList)
mid=0

def NthSmallest(lst, N):
    count=0
    start = min(lst)
    end = max(lst)
    while True:
        mid = (start+end)//2
        #print "mid is " + str(mid)
        smaller_counter = 0
        equal_counter = 0
        for num in lst:
            if num < mid:
                #print str(num) +  " smaller than mid " + str(mid) 
                smaller_counter += 1
            if num <= mid:
                #print str(num) +  " equal to mid " + str(mid)
                equal_counter += 1
        
        if equal_counter >=N and smaller_counter < N:
            print "Nth smallest is   " + str(mid)
            return mid
        
        elif smaller_counter >= N:
            end = mid - 1
        
        else:
            start = mid + 1
        
    
NthSmallest(randomList,nth)
