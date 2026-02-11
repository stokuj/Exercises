def dict_of_numbers() -> dict:
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    result = {}
    
    for i in range(100):
        if i < 20:
            result[i] = ones[i]
        else:
            one_part = i % 10
            ten_part = i // 10
                        
            if one_part == 0:
                result[i] = tens[ten_part]
            else:
                result[i] = f"{tens[ten_part]}-{ones[one_part]}"
            
            
    return result
