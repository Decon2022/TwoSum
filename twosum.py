def twoSum(self, nums: List[int], target: int) -> List[int]:
    #Initialize an empty dictionary to store value and their index
        prevMap= {} # val : index
    
    #Loop through the list 'nums' with index 'i' and number 'n'
        for i, n in enumerate(nums):
            
            #calculate the difference between target and the current number 
            diff = target - n 
            
            #Check if the difference exist in the previously seen number (prevMap)
            if diff in prevMap:
                
                #if the difference exist, return the indices of the complement (diff) and current number
                return [prevMap[diff], i]
            
            #if the difference doesnt exit, add the current number and its index to prevMap
            prevMap[n] = i
            
            #if nothing is found return none
        return 