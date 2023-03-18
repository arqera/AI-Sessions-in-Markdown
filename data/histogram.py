import re
import matplotlib.pyplot as plt

# Regular expression to match numbers
num_regex = r"\b\d+\b"

# Open the text file for reading
with open("Humanity_and_the_Environmen.txt", "r") as f:
    # Read the lines from the file
    lines = f.readlines()

    # Filter the lines for the years after 1999
    filtered_lines = [line for line in lines if "1999" in line]

    # Initialize a dictionary to store the digit frequencies
    digit_freqs = {str(i): 0 for i in range(10)}

    # Loop through the filtered lines
    for line in filtered_lines:
        # Find all numbers in the line using regex
        numbers = re.findall(num_regex, line)
        # Loop through the numbers and count the digits
        for num in numbers:
            for digit in num:
                digit_freqs[digit] += 1

    # Plot the histogram
    plt.bar(digit_freqs.keys(), digit_freqs.values())
    plt.title("Frequency of Digits 0-9 in Numbers After 1999")
    plt.xlabel("Digits")
    plt.ylabel("Frequency")
    plt.show()

