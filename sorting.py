# List of tuples (name, age)
students = [
    ("Alice", 22),
    ("Bob", 19),
    ("Charlie", 25),
    ("Diana", 20)
]

print("Original:", students)

# Sort by age (second element) using lambda
students.sort(key=lambda x: x[1])
print("Sorted by age:", students)

# Sort by name (first element)
students.sort(key=lambda x: x[(0))
print("Sorted by name:", students)
