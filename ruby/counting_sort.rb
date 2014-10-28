# Enter your code here. Read input from STDIN. Print output to STDOUT
list_size = gets.chomp.to_i

counts = Hash.new(0)
input = gets.chomp
numbers = input.split(" ")

numbers.each do |num|
    counts[num.to_i] += 1
end

100.times {|i| print "#{counts[i]} "}
