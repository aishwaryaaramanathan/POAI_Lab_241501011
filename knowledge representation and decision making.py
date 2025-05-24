def minimum(x, y):
    return x if x <= y else y
def maximum(x, y):
    return x if x >= y else y

print("Minimum of 5 and 10:", minimum(5, 10))
print("Maximum of 5 and 10:", maximum(5, 10))
print("Minimum of 8 and 3:", minimum(8, 3))
print("Maximum of 8 and 3:", maximum(8, 3))


likes_map = {
    "mary": {"food", "wine"},
    "john": {"wine", "mary"}}

def likes(person, thing):
    if thing in likes_map.get(person, set()):
        return True
    if person == "john" and thing in likes_map.get("mary", set()):
        return True
    if person == "john" and isinstance(thing, str) and "wine" in likes_map.get(thing, set()):
        return True
    if person == "john" and isinstance(thing, str) and thing in likes_map.get(thing, set()):
        return True
    return False

print("Does John like food?", likes("john", "food"))
print("Does John like wine?", likes("john", "wine"))
print("Who does John like?")
people = {"mary", "john", "food", "wine"}

for person in people:
    if likes("john", person):
        print(" -", person)

