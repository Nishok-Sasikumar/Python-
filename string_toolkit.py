text = input("Enter a sentence: ")

print("Uppercase =", text.upper())
print("Lowercase =", text.lower())
print("Title Case =", text.title())
print("Total Characters =", len(text))
print("Word Count =", len(text.split()))
print("Reversed Sentence =", text[::-1])