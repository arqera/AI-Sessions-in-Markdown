import matplotlib.pyplot as plt
import numpy as np

digit_freqs = {str(i): 0 for i in range(10)}

with open("Humanity_and_the_Environmen.txt") as f:
    for line in f:
        if int(line[:4]) > 1999:
            for char in line:
                if char.isdigit():
                    digit_freqs[char] += 1

fig, ax = plt.subplots()
ax.bar(digit_freqs.keys(), digit_freqs.values())
ax.set_xlabel('Digit')
ax.set_ylabel('Frequency')
ax.set_title('Frequency of Digits in Humanity and the Environment Dataset')
plt.show()

