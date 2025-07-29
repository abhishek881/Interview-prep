print("Hello World")

def has_duplicates(s) :
    seen = set()
    for char in s :
        if s in seen :
            return True
        seen.add(s)
    return False

def missing_number(s) :
    for i in s :
        diff = s[i] - s[i-1]
        if diff != 1 :
            return s[i] -1

nums = [1,2,3,5,6,7]
print(missing_number(nums))        

def two_sum(num, target) :
    num_to_index = {}
    for index,number in enumerate(num) : 
        complement = target - number

        if complement in num_to_index :
            return [num_to_index[complement], index]
        
        num_to_index[complement] = index

    
    return None



#num = [5,7,11,14]





if __name__ == '__main__' :
    print(has_duplicates("hello"))
    nums = [1,2,3,5,6,7]
    print(missing_number(nums))

    