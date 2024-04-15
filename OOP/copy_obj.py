from copy import deepcopy


letters = [1, 2,3,4,]

copy_letters = letters

#change letters and see the difference in shallow copies

copy_letters[3] = 2000


digits = [2,3,4,4,4,4]

deep_copy_digits = deepcopy(digits)

#change digits and see it does not effect the original digits as it has separate reference

deep_copy_digits[3] = 3000


print("Shallow copy", letters, copy_letters)
print("Deep copy", digits, deep_copy_digits)