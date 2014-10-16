# calculate the offsets of letters, passed as numbers
def letter_offset(letter1, letter2)
    result = (letter1 - letter2).abs
end

num_tests = gets.chomp.to_i
num_tests.times do
  count = 0
  string = gets.chomp
  letters = string.split ""
  endpoint = letters.length-1
  # calculate the midpoint of the word, and only consider letters that come after.
  midpoint = letters.length/2
  midpoint += 1 unless letters.length.even?

  # working outside-in, determine the offset between the letters
  endpoint.downto(midpoint) do |i|
      # add the numerical difference of the letters to the running total
      count += letter_offset(letters[endpoint-i].ord, letters[i].ord)
  end
  puts count
end
