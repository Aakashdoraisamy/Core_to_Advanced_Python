t = (1, 2, 3, 4, 5)
remove_element = 3

t = (1, 2, 3, 4, 5)
remove_element = 3

new_t = ()  # empty tuple

for elem in t:
    if elem != remove_element:
        new_t += (elem,)  # add element as a tuple

print("Original tuple:", t)
print("New tuple:", new_t)

"""
🔹 Logic Step by Step

Start with the original tuple

t = (1, 2, 3, 4, 5)
remove_element = 3


Create an empty tuple to store the result

new_t = ()


Iterate through each element in the original tuple

for elem in t:


Check if the element is the one to remove

if elem != remove_element:


If it is not the element to remove, add it to the new tuple

new_t += (elem,)


Result: new_t contains all elements except the one we wanted to remove

🔹 Key Points

Tuples cannot be modified → must build a new tuple

Use += (elem,) to concatenate a single-element tuple

Works for all elements or can be modified to remove only the first occurrence

"""