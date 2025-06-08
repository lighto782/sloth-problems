# https://slothbytes.beehiiv.com/p/memory-leaks


def next_letters(x):
    if x == "":
        return "A"

    base = ord('A') - 1
    chain = [ord(c) - base for c in x]

    chain[-1] += 1

    for i in reversed(range(len(chain))):
        if chain[i] > 26:
            chain[i] -= 26
            if i == 0:
                chain.insert(0, 1)
            else:
                chain[i - 1] += 1

    result = ''.join(chr(c + base) for c in chain)
    return result

letter = input("Enter your chain of letters: ")
print(next_letters(letter))

