import sys


def found_idx(left,right,time):
   
    if time==0 :
        if first_item == 1:
            return (1,1),[1,0,0]
        elif first_item == 2:
            return (2,2), [0,1,0]
        else:
            return (3,3), [0,0,1]
    else:
        want_to_know, count = found_idx(left//3,right//3,time-1)
        
        count_1 = count[0]*1 + count[1]*2
        count_2 = count[0]*1 + count[1]*1 +count[2]*2
        count_3 = count[0]*1 + count[2]*1
  
        left_remain = left%3
        right_remain = right%3
      
        if left_remain == 1:
            if want_to_know[0] == 1:
                count_1 -= 1
                left = 3
            elif want_to_know[0] == 2:
                count_2 -= 1
                left = 1
            else:
                count_2 -= 1
                left = 3
        elif left_remain == 2:
            if want_to_know[0] == 1:
                count_1 -= 1
                count_3 -= 1
                left = 2
            elif want_to_know[0] == 2:
                count_2 -= 1
                count_1 -=1
                left = 1
            else:
                count_2 -= 1
                count_3 -= 1
                left = 2
        else:
            if want_to_know[0] == 1:
                left = 1
            elif want_to_know[0] == 2:
                left = 2
            else:
                left = 2
        if right_remain == 0:
            if want_to_know[1] == 1:
                count_3 -= 1
                count_2 -= 1
                right = 1
            elif want_to_know[1] == 2:
                count_1 -=2
                right = 2
            else:
                count_2 -= 1
                count_3 -= 1
                right = 2
        elif right_remain == 1:
            if want_to_know[1] == 1:
                count_2 -=1
                right = 3
            elif want_to_know[1] == 2:
                count_1 -= 1
                right = 1
            else:
                count_2 -= 1
                right = 3
        else:
            if want_to_know[1] == 1:
                right = 2
            elif want_to_know[1] == 2:
                right = 1
            else:
                right = 2
        
        
        return (left,right), [count_1,count_2,count_3]
first_item = int(sys.stdin.readline())

left_idx = int(sys.stdin.readline())

right_idx = int(sys.stdin.readline())

n = int(sys.stdin.readline())



a,b = found_idx(left_idx,right_idx,n)
print(b[0],b[1],b[2])