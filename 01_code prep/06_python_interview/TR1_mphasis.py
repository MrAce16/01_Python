def count_vowels_and_positions(str_input):
    vowels = "aeiou"
    vowels_position = {}

    for i,j in enumerate(str_input):
        if j in vowels:
            if j not in vowels_position:
                vowels_position[j] = []
            vowels_position[j].append(i+1)
    
    for vowels, position in vowels_position.items():
        print(f"'{vowels}' appers in str {len(position)} : {position}")



str_input = "raghunath"
count_vowels_and_positions(str_input)