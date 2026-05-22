# Rule-Based AI Chatbot (Project 1)

A rule-based AI chatbot GUI built with Python and Tkinter. **Unit-42** uses deterministic intent rules (no ML/API) with traceable Input → Logic → Output flow.

## Features

- GUI chat interface (Catppuccin-style theme)
- Rule-based intent recognition
- Deterministic responses and conversation state
- Input sanitization
- Help flow (basic / advanced)

## Technologies

- Python 3
- Tkinter (stdlib)

## Project structure

```
Project_1_Chatbot/
├── chatbot.py
├── README.md
├── Screenshot .png
└── Screenshot 2.png
```

## How to run

1. Install [Python 3](https://www.python.org/downloads/) (Tkinter is included on Windows/macOS with the default installer).
2. Open a terminal in this folder (`Project_1_Chatbot`).
3. Run:

```bash
python chatbot.py
```

## Sample intents

| You can try | Expected behavior |
|-------------|-------------------|
| `hello`, `hi` | Greeting |
| `who are you` | Identity |
| `tell me a joke` | Joke |
| `weather` | Weather (rule-based reply) |
| `help` | Basic or advanced help prompt |
| `exit`, `bye` | Closes the app |

## Screenshots

![Chatbot interface](Screenshot%20.png)

![Conversation example](Screenshot%202.png)

## Author

Sahithi Manda

## Repository

[Rule-Based-AI-Chatbot](https://github.com/sahithi-manda/Rule-Based-AI-Chatbot)
