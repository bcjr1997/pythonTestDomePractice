def unique_names(names1, names2):
    names_set = set(names1)
    for name in names2:
        if name not in names_set:
            names_set.add(name)
    return list(names_set) or None

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
