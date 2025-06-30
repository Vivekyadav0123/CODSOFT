import datetime
import random

#word meanings
dictionary = {
    "python": "a programming language.",
    "ai": "simulation of human intelligence.",
    "chatbot": "a program that interacts via text."
}

#motivational quotes
quotes = [
    "Keep pushing forward.",
    "Small steps every day.",
    "Believe in yourself.",
]

print("SmartBot Activated! (type 'help' for options, 'exit' to quit)\n")

for _ in range(500):
    msg = input("You: ").lower()

    if "hi" in msg or "hello" in msg:
        print("Bot: Hi there! I'm SmartBot.")
    elif "name" in msg:
        print("Bot: I'm SmartBot, your Python chatbot.")
    elif "time" in msg:
        print("Bot:", datetime.datetime.now().strftime("Current time: %I:%M %p"))
    elif "date" in msg:
        print("Bot:", datetime.date.today().strftime("Date: %d %B %Y"))
    elif "day" in msg:
        print("Bot:", f"Today is {datetime.datetime.now().strftime('%A')}")
    elif "quote" in msg or "motivate" in msg:
        print("Bot:", random.choice(quotes))
    elif any(op in msg for op in "+-*/"):
        try:
            result = eval(msg)
            print("Bot: Result is", result)
        except:
            print("Bot: Invalid expression.")
    elif "meaning of" in msg:
        word = msg.split("meaning of")[-1].strip()
        print("Bot:", dictionary.get(word, "Sorry, I don't have that word."))
    elif "help" in msg:
        print("""Bot: Try these commands:
- hello / hi
- time / date / day
- calculate (e.g. 4 + 5)
- meaning of ai / python
- quote / motivate me
- exit
""")
    elif "exit" in msg or "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I didn't get that. Type 'help' to see what I can do.")
