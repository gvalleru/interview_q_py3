import threeSum

test_data = [[-1, 0, 1, 2, -1, 4],
             [1, 2, 3, 0, -1, -2, 5, 7, 3],
             [5, -5, -4, -1, 7, -2]
             ]
x = threeSum.Solution()

for l in test_data:
    print("3 sum for list: " + str(l))
    print(x.threeSum(l, 1))
