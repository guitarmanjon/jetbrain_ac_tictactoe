no_lines = int(input())
winners = []
for _n in range(no_lines):
    entry = input().split(" ")
    if entry[1] == "win":
        winners.append(entry[0])

print(winners)
print(len(winners))
