import split_array_two

test_data = [[1, 4, 3, 8],
             [5, 2, 1, 3, 3],
             [2, 7, 3, 2, 1, 3],
             [1, 3, 2, 9]
             ]

#test_data = [[1, 4, 3, 8]]
for i in test_data:
    x = split_array_two.Solution(i)
    print(x.split_array_two())
