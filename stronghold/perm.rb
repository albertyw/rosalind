n = 5

# Recursively get permutations
def get_permutations(digits)
  return [digits] if digits.length == 1
  permutations = []
  digits.each_with_index do |digit, index|
    digits_left = digits.rotate(index+1)[0,digits.length-1]
    permutations_left = get_permutations(digits_left)
    permutations_left.map!{|permutation| [digit]+permutation}
    permutations += permutations_left
  end
  return permutations
end

digits = (1..n).to_a
permutations =  get_permutations(digits)

# Print out permutations
p permutations.length
permutations.each do |permutation|
  permutation.each do |digit|
    print digit.to_s+' '
  end
  print "\n"
end
