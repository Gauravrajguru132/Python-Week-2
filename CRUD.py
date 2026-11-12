# Create
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Read
print("First item:", fruits[0])
print("All items:", fruits)

# Update
fruits[1] = "blueberry"
print("After update:", fruits)

# Delete
fruits.remove("cherry")          # by value
del fruits[0]                    # by index
print("After delete:", fruits)

# Add (extra useful operations)
fruits.append("mango")
fruits.insert(0, "kiwi")
print("After adding:", fruits)
