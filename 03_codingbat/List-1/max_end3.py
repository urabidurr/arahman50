def max_end3(nums):
  c = nums[0] if nums[0] > nums[len(nums)-1] else nums[len(nums)-1]
  return [c, c, c]

