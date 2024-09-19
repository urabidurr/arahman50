def centered_average(nums):
  sum = 0
  mi = nums[0]
  mp = nums[0]
  
  for i in range(0,len(nums)-1):
    mi = min(mi,nums[i+1])
    
  for j in range(0,len(nums)-1):
    mp = max(mp,nums[j+1])
  
  for k in nums:
    sum += k
  
  sum -= (mi+mp)
  
  return sum / (len(nums)-2)
