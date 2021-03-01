numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = [number for number in numbers if number % 2 == 0] #[2, 4, 6, 8]

odd_numbers = [number for number in numbers if number % 2 != 0] #[1, 3, 5, 7, 9]

# [_if_true_result_  _if_condition_ else _else_result for value in values]
fun_list = [number * 2 if number % 2 == 0 else number/2 for number in numbers] #[0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5]


with_vowels = "This is a sentence with vowel."
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou") #Ths s  sntnc wth vwl.
