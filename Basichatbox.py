import random
import time


brain = {
    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How do you get comforted by a JavaScript bug? You console it.",
        "Why was the cell phone wearing glasses? It lost its contacts.",
        "What’s a programmer’s favorite hangout place? The Foo Bar.",
        "What do you call a fake noodle? An Impasta!",
        "Why don't scientists trust atoms? Because they make up everything!"
    ],
    "topics": {
        "happy": {
            "replies": ["That's the spirit!", "Your joy is contagious!", "I'm happy because you're happy!"],
            "follow_ups": ["What's the best thing that happened today?", "Do you think this mood will last all week?", "Who is the first person you want to share this news with?"]
        },
        "sad": {
            "replies": ["I'm here for you.", "It's okay to feel this way.", "I wish I could help more."],
            "follow_ups": ["Do you want to talk more about what happened?", "Would a joke help, or do you just need someone to listen?", "What's one small thing that usually makes you feel better?"]
        },
        "excited": {
            "replies": ["Let's go!!", "That sounds legendary!", "I'm hyped just reading that!"],
            "follow_ups": ["When is this happening?", "Are you fully prepared for it?", "On a scale of 1 to 10, how big is this?"]
        },
        "nervous": {
            "replies": ["Take a deep breath.", "You've got this, I promise.", "Jitters are just energy."],
            "follow_ups": ["What part of it is making you most anxious?", "Have you done something like this before?", "Can I give you a tip to calm your nerves?"]
        }
    }
}


context = {"last_topic": None, "used_jokes": []}

def get_joke():
    available = [j for j in brain["jokes"] if j not in context["used_jokes"]]
    if not available:
        context["used_jokes"] = []
        available = brain["jokes"]
    joke = random.choice(available)
    context["used_jokes"].append(joke)
    return joke

def chatbot_logic(user_input):
    text = user_input.lower().strip()
    
   
    for emotion in brain["topics"]:
        if emotion in text:
            context["last_topic"] = emotion
            reply = random.choice(brain["topics"][emotion]["replies"])
            question = random.choice(brain["topics"][emotion]["follow_ups"])
            return f"{reply} {question}"


    if any(w in text for w in ["joke", "laugh", "funny"]):
        return f"Here's a fresh one: {get_joke()}. Did you like that one?"

    
    if context["last_topic"]:
        topic = context["last_topic"]
        if any(w in text for w in ["yes", "yeah", "sure", "maybe", "ok"]):
            return f"I'm glad we're on the same page. Tell me more about why you feel {topic}."
        elif any(w in text for word in ["no", "not", "nope"]):
            return f"I understand. If not that, then what is making you feel {topic}?"


    return random.choice([
        "I'm all ears. What else is on your mind?",
        "By the way, I was thinking—do you usually have days like this?",
        "That's interesting. Does this happen often?",
        "I'm curious, what's your favorite way to spend a day like today?"
    ])

def start_chat():
    print("--- HUMAN-LEVEL CHATBOT v5.0 ---")
    print("Bot: Hey! I've been waiting to chat. How are you feeling right now?")
    
    while True:
        user_msg = input("You: ")
        if any(w in user_msg.lower() for w in ["bye", "exit"]):
            print("Bot: It was great talking to you. Come back soon!")
            break
        
       
        print("Bot is typing", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")
        
        response = chatbot_logic(user_msg)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    start_chat()
