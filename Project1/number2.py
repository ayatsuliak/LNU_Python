lol = [['k', 'a', 'a', 'r'], ['w', 'u', 'k'], ['a', 'k', 'a'], ['w', 'a', 't', 'a', 'k'], ['a', 'b']]
def consonant(list):
    vowels = "AaEeOoIiUu"
    new_list = []
    for k in list:
        found = False
        sub_list = []
        for i in range(len(k)):
            if k[i] not in vowels:
                for j in range(len(k) - 1, i - 1, -1):
                    if k[j] not in vowels:
                        sub_list = k[i:j + 1]
                        found = True
                        break
                if found:
                    break
        new_list.append(sub_list)
    return sorted(new_list, key=lambda x: len(x))
print(consonant(lol))

def is_alternate(sequence):
    if len(sequence) < 2:
        return False
    vowels = "AaEeOoIiUu"
    for i in range(len(sequence) - 1):
        if (sequence[i] not in vowels and sequence[i+1] not in vowels) or (sequence[i] in vowels and sequence[i+1] in vowels):
            return False
    return True

def consonant_vowel(list):
    new_list = []
    for k in list:
        found = False
        sub_list = []
        for i in range(len(k)):
            for j in range(len(k) - 1, i, -1):
                if is_alternate(k[i:j + 1]):
                    sub_list = k[i:j + 1]
                    found = True
                    break
            if found:
                break
        new_list.append(sub_list)
    return sorted(new_list, key=lambda x: len(x))
print(consonant_vowel(lol))