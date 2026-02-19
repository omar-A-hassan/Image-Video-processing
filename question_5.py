user_list = input("Enter your list items separated by a space: ").split()

print(f"Your initial list {user_list}")

no_dups_set = set()

no_dups_list = []

for item in user_list:
    if item not in no_dups_set:
        no_dups_list.append(item)
        no_dups_set.add(item)

print(f"your no dups list {no_dups_list}")