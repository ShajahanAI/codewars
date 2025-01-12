def isHappy(n, pow):
    nums = []
    while True:
        nums.append(n)
        n = sum([d**pow for d in map(int, str(n))])
        if n == 1:
            return [1]
        if n in nums:
            return nums[nums.index(n):] + [n]

output = isHappy(7, 2)
print(output)