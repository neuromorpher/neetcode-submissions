class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        seqs = []
        
        for num in nums:

            curSeq = []
            if (num-1) not in num_set: # must be the start of a sequence 
            
                curSeq.append(num)
                nextNum = num 
                while nextNum+1 in num_set:

                        nextNum += 1 
                        curSeq.append(nextNum)
                seqs.append(len(curSeq))

        return max(seqs) if seqs else 0 

        
                


    
            
        


        