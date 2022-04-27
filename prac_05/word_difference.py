

first_word = "willy"
second_word = "shall"

first_chars = list(first_word)
second_chars = list(second_word)

print(first_chars)
print(second_chars)

difference_chars = []
for i in range(len(first_chars)):
    for j in range(len(second_chars)):
        if [first_chars[i], j] in difference_chars:
            continue
        else:
            if first_chars[i] == second_chars[j]:
                difference_chars.append([first_chars[i], j])

print(difference_chars)