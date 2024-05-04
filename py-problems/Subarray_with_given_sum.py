#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        sum=0
        start=0
        for curr in range(0,n):
            sum+=arr[curr]
            if s == sum:
                return(start+1,curr+1)
            elif sum>s:
                sum-=arr[start]
                start+=1
                if s == sum:
                    return(start+1,curr+1)
                
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends