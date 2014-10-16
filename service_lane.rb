# get input from the program
input= gets.chomp
problem_dimensions = input.split(" ")
# split problem dimensions from initial input
freeway_length = problem_dimensions[0]
num_test_cases = problem_dimensions[1].to_i

# get array of freeway lengths
array_input = gets.chomp
widths = array_input.split(" ")
# convert to ints
widths.collect! {|w| w.to_i}

num_test_cases.times do
  range_input = gets.chomp
  ranges = range_input.split(" ")
  range_start = ranges[0].to_i
  range_stop = ranges[1].to_i
  puts widths[range_start..range_stop].min
end
