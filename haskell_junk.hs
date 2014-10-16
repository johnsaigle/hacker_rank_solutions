-- Get the absolute value of all elements in a list
f arr = [abs(x) | x <- arr]

-- Determine the length of a list without using any built in functions
len :: [a] -> Int
len lst = sum [1 | _ <- lst]
