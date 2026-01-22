height = [0,2,0,3,1,0,1,3,2,1]


def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    res = 0

    while l < r:
        if maxLeft < maxRight:
            l += 1
            if maxLeft < height[l]:
                maxLeft = height[l]
            res += maxLeft - height[l]
        else:
            r -= 1
            if maxRight < height[r]:
                maxRight = height[r]
            res += maxRight - height[r]
    
    return res 

print(trap(height))