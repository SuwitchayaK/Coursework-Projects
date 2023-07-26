#Exercise 1
def Exercise1(nums):
      '''create empty arrays L and R'''
      L = [None] * len(nums)
      R = [None] * len(nums)
      '''initialize value in two arrays'''
      L[0] = 1
      R[len(nums) - 1] = 1
      '''create elements in the rest of array L'''
      for i in range(1,len(nums)):
              L[i] = L[i - 1] * nums[i - 1]
      '''create elements in the rest of array R'''
      for i in range(len(nums) - 2, -1, -1):
              R[i] = R[i + 1] * nums[i + 1]
      '''elements calculated from the product of the two arrays'''
      for i in range(len(nums)):
         L[i] = L[i] * R[i]
      return L

#Exercise 2
def Exercise2(matrix):
      result = []
      '''set left and right pointers where the length is the number of
      column'''
      left, right = 0, len(matrix[0])
      '''set top and bottom pointers where the length is the number of
      rows'''
      top, bottom = 0, len(matrix)
      '''create the loop that the pointers will bot cross each other'''
      while left < right and top < bottom:
            #numbers in the top row
            for i in range(left, right):
                  '''append elements in each column in the top row''' 
                  result.append(matrix[top][i])
            '''shift the top pointer down'''
            top += 1
            #numbers in the right most column
            for i in range(top, bottom):
                  '''get elements in the right column excluding first element'''
                  result.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                  break
            #numbers in bottom row
            '''go from right to left in reverse order'''
            for i in range(right - 1, left - 1, -1):
                  result.append(matrix[bottom - 1][i])
            bottom -= 1
            #numbers in left most column
            '''go from bottom to top in reverse order'''
            for i in range(bottom - 1, top - 1, -1):
                  result.append(matrix[i][left])
            left += 1
      return result

#Exercise 3
def Exercise3(nums1, nums2, nums3, nums4):

        d = {}
        count = 0
        '''first nested loop to store all combinations of sum from two arrays''' 
        for i in nums1:
            for j in nums2:
                d[i + j] = d.get(i + j, 0) + 1
        '''iterate the other two arrays'''
        for k in nums3:
            for l in nums4:
                count += d.get(-(k + l), 0)
        return count

#Exercise 4
def Exercise4(height):
        result = 0
        '''initialize left and right pointers'''
        left, right = 0, len(height) -1
        while left < right:
                area = (right - 1) * min(height[left], height[right])
                result = max(result, area)
                #shift left pointer to the right
                if height[left] < height[right]:
                        left += 1
                #shift right pointer to the left
                elif height[left] > height[right]:
                        right -= 1
                #when pointers are equal move either left or right pointer
                else:
                        right -= 1
        return result

#Exercise 5
def Exercise5(nums):
      '''sort all numbers before finding the consecutives'''
      nums = sorted(nums)
      '''longest is the longest consecutive numbers now set it 0, it will be
      added later after there are consecutive numbers'''
      longest = 0
      for i in nums:
            '''if there is no other consecutive number before i, the length
            remains 0'''
            if (i - 1) not in nums:
                  length = 0
                  '''add up to length if there is a number before i'''
                  while (i + length) in nums:
                        length += 1
                  '''keep updating the longest consecutives'''
                  longest = max(length, longest)
      return longest

#Exercise 6
def Exercise6(nums):
      '''sort numbers so the the duplicate number will be next to each other'''
      nums = sorted(nums)
      '''select number i from numbers''' 
      for i in range(len(nums)):
            '''there is only one repeated number, so there is only one time
            that i will be equal to the next number'''
            if nums[i] == nums[i + 1]:
                  return nums[i]

#Exercise 7
def Exercise7(s,k):
      '''create window boundaries left and right'''
      left, right = 0, 0
      '''create dictionary that will contain characters and their frequencies'''
      char = dict()
      '''create variable for the longest substring'''
      length = 0
      '''expand the window'''
      while right < len(s):
            if s[right] not in char:
                  k -= 1
            char[s[right]] = right
            '''shrink the window'''
            while k < 0:
                  if char[s[left]] == left:
                        k += 1
                  left += 1

            length = max(length, right - left + 1)
            right += 1
      return length

#Exercise 8
from collections import deque
def Exercise8(nums, k):
      '''create list for the result'''
      result = []
      '''initializing deque'''
      q = deque()
      '''set left and right pointers at the very beginning'''
      left = right = 0
      while right < len(nums):
            '''remove smaller values from deque'''
            while q and nums[q[-1]] < nums[right]:
                  q.pop()
            q.append(right)
            '''remove left element from window'''
            if left > q[0]:
                  '''reomove the left element of the deque'''
                  q.popleft()
            '''to ensure that the window is at least size k'''
            if (right + 1) >= k:
                  '''append the maximum value into the result'''
                  result.append(nums[q[0]])
                  '''the left pointer will be added up only when the
                  window is at least size k'''
                  left += 1
            '''the right pointer added up after the loop is done'''
            right += 1
      return result

#Exercise 9
def Exercise9(s, t):
      if t == "": return ""
      '''create hash map'''
      countT, window = {}, {}
      for char in t:
            countT[char] = 1 + countT.get(char, 0)

      have, missing = 0, len(countT)
      result, reslen = [-1, -1], float("infinity")
      left = 0
      '''right pointer of the window'''
      for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                  have += 1

            while have == missing:
                  '''size of the current window less than the current result
                  length, update the result'''
                  if (right - left + 1) < reslen:
                        result = [left, right]
                        reslen = (right - left + 1)
                  '''minimize window by popping the left character'''
                  window[s[left]] -= 1
                  if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                  left += 1
      left, right = result
      return s[left:right+1] if reslen != float("infinity") else ""
