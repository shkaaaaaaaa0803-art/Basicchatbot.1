# Basicchatbot.1
A rule-based conversational agent built in Python that uses state management and sentiment dictionaries to simulate human-like interaction. This bot doesn't just respond to keywords; it tracks conversation history to ask proactive follow-up questions.

🌟 Features
Contextual Memory: Remembers the last topic discussed (e.g., if you are feeling sad, it keeps the conversation supportive).

Emotion Detection: Includes specialized dictionaries for Happy, Sad, Excited, and Nervous moods.

Infinite Joke Engine: A non-repeating randomization system that ensures you don't hear the same joke twice.

Proactive Conversation: Unlike standard bots, this one asks questions back to the user to keep the dialogue alive.

Time-Aware Greetings: Greets the user based on the actual time of day (Morning, Afternoon, Evening).

🧠 How It Works
The bot operates on a Linear Priority Logic system:

Normalization: Cleans user input (lowercase/strip).

Sentiment Mapping: Loops through emotional dictionaries to find keyword matches.

State Check: If no new keyword is found, it checks the context variable to continue the previous topic.

Fallback: If all else fails, it uses "Open-Ended" questions to encourage the user to speak more.

🛠️ Tech Stack
Language: Python 3.x

Logic: Conditional branching (if-elif-else) and Nested Dictionaries.

Libraries: random (for variety), time (for typing simulation), and datetime (for time-awareness).

🚀 Getting Started
Prerequisites
Python 3 installed on your machine.

Installation & Usage
Clone the repository:

Bash

git clone https://github.com/shkaaaaaaaa0803-art/Basicchatbot.git
Navigate to the directory:

Bash

cd Basicchatbot
Run the bot:

Bash

python main.py
📝 Example Interaction
User: I am feeling a bit nervous today.

Bot: Take a deep breath. You've got this! Is it a big event or just a general feeling?

User: A big event.

Bot: I see. Since you're nervous about this event, would you like a quick tip to calm your jitters?
