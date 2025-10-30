def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]
nums=list(map(int,input().split()))

def rob(nums):
    memo = {}
    
    def dp(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        
        # Choice: rob this house OR skip it
        rob_this = nums[i] + dp(i+2)
        skip_this = dp(i+1)
        
        memo[i] = max(rob_this, skip_this)
        return memo[i]
    
    return dp(0)
