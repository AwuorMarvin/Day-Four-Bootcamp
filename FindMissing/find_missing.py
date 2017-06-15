def find_missing(arg1, arg2):
    total_arg1 = 0
    total_arg2 = 0
  
    if len(arg1) == 0 and len(arg2) == 0:
        return 0
    else:
        for i in arg1:
            total_arg1+=i
        for j in arg2:
            total_arg2+=j
        
        return abs(total_arg2 - total_arg1)
  
find_missing([1,2,3], [1,2,3,4])