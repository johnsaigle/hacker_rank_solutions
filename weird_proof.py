def my_function(n):
  return (n ** (n/(n-1)))

results = []

# don't check i = 1 because it gives us a divide by zero
while True:
    upper_bound = int(input("Enter the upper bound for the domain: "))
    try:
        upper_bound = int(upper_bound)
    except TypeError:
        continue
    break

for i in range(2, upper_bound + 1):
  results.append(my_function(i))

results = filter(lambda x: float(x).is_integer(), results)

print ("Results that satisfy our equation, after selecting only whole numbers: ")
for r in results:
  print (r)
