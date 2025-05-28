import json
import os
import difflib

# File path for English JSON memory
MEMORY_FILE = "hafiza_en.json"

# Load memory from JSON file
def load_memory(file=MEMORY_FILE):
    try:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as file:
                return json.load(file)
        # If file doesn't exist, initialize empty JSON
        return {"name": None, "favorites": {}, "conversations": {}}
    except json.JSONDecodeError:
        print("JSON is corrupted, creating a new one!")
        return {"name": None, "favorites": {}, "conversations": {}}

# Save memory to JSON file
def save_memory(memory, file=MEMORY_FILE):
    with open(file, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)

# Find closest matching response
def find_closest_response(question, memory):
    matches = difflib.get_close_matches(question, memory["conversations"].keys(), n=1, cutoff=0.7)
    return memory["conversations"][matches[0]] if matches else None

# Chat function
def chat(question):
    global memory
    memory = load_memory()
    name = memory["name"] or "Unknown person"

    # Learn name
    if "my name is" in question:
        name = question.replace("my name is", "").strip().capitalize()
        memory["name"] = name
        save_memory(memory)
        return f"Nice to meet you, {name}!"

    # Find similar response
    response = find_closest_response(question, memory)
    if response:
        return response

    # If unknown, learn new response
    answer = input(f"{name}, I don’t know this. What should I say? ")
    memory["conversations"][question] = answer
    save_memory(memory)
    return "Got it, learned!"

# Test
if __name__ == "__main__":
    while True:
        message = input("Ask away: ").strip().lower()
        if message == "q":
            print("See you later!")
            break
        print(f"soly: {chat(message)}")