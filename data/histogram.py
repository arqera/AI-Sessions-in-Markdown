import matplotlib.pyplot as plt

digit_freqs = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

with open('Humanity_and_the_Environmen.txt', 'r') as f:
    for line in f:
        try:
            if int(line[:4]) > 1923:
                for digit in line:
                    if digit.isdigit():
                        digit_freqs[int(digit)] += 1
        except ValueError:
            continue

plt.bar(digit_freqs.keys(), digit_freqs.values())
plt.show()

