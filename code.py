import heapq
class Solution:
    def nextPermutation(self, arr):
        # if len(arr) <= 1:
        #     return arr
            
        # turn_index = -1
        # for i in range(len(arr)-2, -1, -1):
        #     if arr[i] < arr[i+1]:
        #         turn_index = i
        #         break
        
        # if turn_index ==-1:
        #     arr.sort()
        #     return arr
            
        # # sort the subarray
        # heap = [] 
        # for i in range(turn_index,len(arr)):
        #     heapq.heappush(heap, arr[i])
        
        # nextSmall = None
        # subres = []
        # while heap:
        #     val = heapq.heappop(heap)
        #     if nextSmall == None and val > arr[turn_index]:
        #         nextSmall = val
        #     else:
        #         subres.append(val)
                
        # arr[:] = arr[0:turn_index] + [nextSmall] + subres
        # return arr
            
        n = len(arr)
        if n < 2:
            return arr
            
        # Finding the turing index 
        turing_index = -1
        for i in range(n-1-1,-1,-1):
             if arr[i] < arr[i+1]:
                 turing_index = i
                 break
        if turing_index == -1:
            arr.sort()
            return arr
            
        # In place replacement for the next largest value
        j = n-1
        while j>turing_index:
            if arr[j] > arr[turing_index]:
                arr[turing_index], arr[j] = arr[j], arr[turing_index]
                break
            j -= 1
        
        # Reverse the subarrary
        arr[turing_index+1:] =reversed(arr[turing_index+1:])
        
        return arr
        
        
        