sentence = input()
sentence_lower = sentence.lower()
sentence1 = sentence_lower.replace(",", "")
sentence1 = sentence1.replace(".", "")
sentence1 = sentence1.replace("!", "")
sentence1 = sentence1.replace("?", "")
print(sentence1)