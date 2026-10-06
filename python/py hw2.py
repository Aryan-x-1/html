paragraph = """Python is a popular programming language.
This Python course teaches beginners the basics of programming.
The course includes variables, strings, loops and functions."""

print("Length:", len(paragraph))

print("First character:", paragraph[0])

print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("After replacing:", paragraph)

paragraph = paragraph.lower()
print("Lowercase:", paragraph)

paragraph = paragraph.strip()

words = paragraph.split()
print("Words:", words)

if "course" in paragraph:
    print("The word 'course' was found.")

print("The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)
))