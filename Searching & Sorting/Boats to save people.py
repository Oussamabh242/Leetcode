class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people , reverse = True )
        
        sum = 0 
        left = 0
        right = len(people)-1
        
        while left<=right :
            if people[right]+people[left]<=limit :
                right -=1
                left+=1
            else : 
                left +=1
            sum +=1
        return sum 
