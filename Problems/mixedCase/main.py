input_words = input().split()
output_words = []

if len(input_words) == 1:
    output_words = input_words
else:
    for n in range(len(input_words)):
        if n == 0:
            output_words.append(input_words[n])
        else:
            output_words.append(input_words[n].title())

output = "".join(output_words)

print(output)
