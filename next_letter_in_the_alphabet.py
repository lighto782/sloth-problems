# https://slothbytes.beehiiv.com/p/memory-leaks

def next_letter(x):
    if x == "":
        return "A"
    else:
        chain = [ord(i.capitalize()) - 64 for i in x]
        chain[-1] += 1
        i = 1
        for i in reversed(range(len(chain))):
            if chain[i] > 26:
                chain[i] -= 26
                if i == len(chain):
                    chain.insert(0, 1)
                else:
                    chain[i-1] += 1
        result = ''.join([chr(i + 64) for i in chain])
        return result

letter = input("Enter your chain of letters: ").strip().upper()
if not letter.isalpha():
    print("Please enter only letters.")
else:
    print(next_letters(letter))

