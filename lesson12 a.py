#day 1
"""
letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])
print(type(letters[1]))
print(type(letters[1:2]))
print(letters[:2])
print(letters[2:])
print(letters[:])


#day 2

letters = ["a", "b", "c", "d", "e"]
letters.append("n")
print(letters)

letters.append("g")
print(letters)

letters.extend(["p", "q", "r"])
print(letters)

letters.insert(2, "z")
print(letters)

letters = ["a", "b", "c", "d", "e"]
letters.extend(["f", "g", "h"])
print(letters)



letters = ["a", "b", "c", "d", "e"]
letters.remove("c")
print(letters)

letters = ["a", "b", "c", "d", "e"]
del letters[3]
print(letters)


letters = ["a", "b", "c", "d", "e"]
lastLetter = letters.pop()
print(letters)
print(lastLetter)

letters = ["a", "b", "c", "d", "e"]
second = letters.pop(1)
print(second)
print(letters)
"""





student = []
student.extend(["a", "b", "c"])
student.append("d")
student.insert(4, "e")
print(student)

student.pop()
student.remove("d")
del student[1]
print(student)
