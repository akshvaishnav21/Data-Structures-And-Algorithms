def bucket_sort(arr):
    d = {}
    for x in arr:
        d[countSetBits(x)] = d.get(countSetBits(x), []) + [x]
    for each_list in sorted(d):
        print(*sorted(d[each_list]))
    
def countSetBits(num): 
  
     # convert given number into binary 
     # output will be like bin(11)=0b1101 
    binary = bin(num) 
  
     # now separate out all 1's from binary string 
     # we need to skip starting two characters 
     # of binary string i.e; 0b 
    setBits = [ones for ones in binary[2:] if ones=='1'] 
    return len(setBits)
n = int(input())
arr = list(map(int, input().split()))
bucket_sort(arr)
