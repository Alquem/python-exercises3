par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for letter in par:
    l = letter.lower()
    if l != " ":
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1

print(counts)