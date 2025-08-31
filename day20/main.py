print("Hello! i am Ai bot. whats your name?")
name = input()

print(f"Nice to meet you, {name}!")

print("How are youfeeling today? (good/bad)")
mood = input()
if mood == "good":
    print("really happy to hear that your feeling good")
elif mood == "bad":
    print("im sorry to hear that, hope things get better")
else:
    print("i see sometimes its hard to put feelings into words")

print(f"It was nice chatting with you {name}. Goodbye!")