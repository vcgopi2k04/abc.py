def most_frequent(text):
    # Create an empty dictionary to store the frequency of each letter
    freq_dict = {}

    # Count the frequency of each letter in the string
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Sort the letters in decreasing order of frequency
    sorted_chars = sorted(freq_dict, key=freq_dict.get, reverse=True)

    # Print the sorted letters and their frequencies
    for char in sorted_chars:
        print(char, "=", freq_dict[char])


text = input("Please enter a string:mississippi ")
most_frequent(text)
#output
i = 4
s = 4
p = 2
m = 1
