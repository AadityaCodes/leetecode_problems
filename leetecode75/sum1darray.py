'''
Purpose:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''

#Define a class
class solution:
    
    #Constructor
    def __init__ (self,numbers):
        self.numbers = numbers
    
    #Adding numbers in the array
    def sum_list(self):
        #For loop to iterate in the array
        for i in range(len(self.numbers)):
            #Break the loop if it goes out of index
            if i+1 == len(self.numbers):
                break
            #Adding numbers
            self.numbers[i+1] = self.numbers[i] + self.numbers[i+1]    
        return self.numbers
        
#Calling the class
answer = solution([1,2,3,4])        
addition = answer.sum_list()
print(addition)