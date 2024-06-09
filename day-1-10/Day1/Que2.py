# You will be given a roman numeral convert it to an integer. 

# Roman numerals are typically written from largest to smallest from left to right
# when smaller numeral appears before a larger numeral, it is substracted.
# when small or equal numeral appears after a larger numeral it is added.

def roman_to_int(roman):
    roman_to_int_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    n = len(roman)
    for i in range(n):
        current_value = roman_to_int_values[roman[i]]
        # if this is not the last character and the next character represents the larger value
        if i < n-1 and current_value < roman_to_int_values[roman[i+1]]:
            total -= current_value
        else:
            total += current_value
    return total

roman_numeral = "MICVX"
print(f"The value of the {roman_numeral} is {roman_to_int(roman_numeral)}.")
            
        
