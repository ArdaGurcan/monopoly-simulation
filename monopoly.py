from matplotlib import pyplot as plt
import random

square = 1
n = 100000

probabilities = [0 for _ in range(40)]

for _ in range(n):
    square += random.randrange(2, 12)  # ADVANCE
    if square > 40:
        square -= 40

    if square in [3, 18, 34]:  # COMMUNITY CHEST CARDS
        card = random.random()

        if card < 1/16:  # go to jail with 1/16 probability
            square = 11
        elif card < 2/16:
            square = 1  # advance to go with 1/16 probability

    if square in [8, 23, 37]:  # CHANCE CARDS
        card = random.random()

        if card < 1/16:  # advance to go with 1/16 probability
            square = 1

        elif card < 3/16:  # advance to nearest station with 2/16 probability
            if square == 8:
                square = 16
            elif square == 23:
                square = 26
            elif square == 37:
                square = 6

        elif card < 4/16:  # go to jail with 1/16 probability
            square = 11

        elif card < 5/16:  # advance to Illinois with 1/16 probability
            square = 25

        elif card < 6/16:  # advance to St. Charles with 1/16 probability
            square = 12

        elif card < 7/16:  # advance to nearest utility with 1/16 probability
            if square == 8:
                square = 13
            elif square == 23:
                square = 29
            elif square == 37:
                square = 13

        elif card < 8/16:  # advance to Reading Railroad with 1/16 probability
            square = 6

        elif card < 9/16:  # advance to Boardwalk with 1/16 probability
            square = 40

        elif card < 10/16:  # go back three squares with 1/16 probability
            square -= 3

    if square == 31 or random.random() < 1/216:  # GO TO JAIL
        square = 11

    probabilities[square - 1] += 1/n  # COUNT


plt.bar([k+1 for k in range(40)], probabilities, color='limegreen')  # PLOT
print(probabilities)
plt.title("Probabilities for Ending Up on Each of the Squares in Monopoly")
plt.xlabel("Index of Square")
plt.ylabel("Probability of Landing on Square")
plt.xticks([k+1 for k in range(40)])
plt.show()
plt.savefig("./bar_plot.png")