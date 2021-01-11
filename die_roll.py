# 1. Die roll 1-6 (return variable)
# 2. Call "die roll" x 5 and return _ _ _ _ _
# 3. Repeat function 2 x 7 (list)
# 4. Take list, return words
import random

# Die roll 1-6 (return variable)
from typing import List


def roll_die() -> int:
    n = random.randint(1, 6)
    # TODO finish random implimitation 1-6
    return n


# Call "die roll" x 5 and return.....
def generate_five_digit_id() -> int:
    buf = ''
    for i in range(0, 5):
        d = roll_die()
        buf = buf + str(d)
    return int(buf)


# Repeat function 2 x 7 (list)
def generate_five_digit_ids(x: int) -> list:
    r = []
    for i in range(x):
        id1 = generate_five_digit_id()
        r.append(id1)
    return r


def find_word(rolls: List[int]) -> List[str]:
    buf = []
    with open('diceware.wordlist.txt', 'r') as word_file:
        for line in word_file:
            for roll in rolls:
                if str(roll) in line:
                    clean_line = line [6:-1]
                    buf.append(clean_line)

    return buf


x = generate_five_digit_ids(7)

print(x, type(x), len(x))
result = find_word(x)
print(result)
