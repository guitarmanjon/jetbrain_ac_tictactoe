in_list = input().split()

out_list = [w for w in in_list if w.endswith("s")]

print("_".join(out_list))
