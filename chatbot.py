import tkinter as tk
from tkinter import scrolledtext
import string

class Unit42GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit-42 Logic Engine Interface")
        self.root.geometry("500x650")
        self.root.configure(bg="#1e1e2e")
        
        self.state_history = []
        self.awaiting_help_spec = False
        
        # Chat History Display
        self.chat_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, state='disabled', bg="#181825",
            fg="#cdd6f4", font=("Consolas", 11), bd=0, padx=15, pady=15
        )
        self.chat_display.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        # Input Frame
        self.input_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.input_frame.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        # Entry Widget
        self.entry = tk.Entry(
            self.input_frame, bg="#313244", fg="#cdd6f4",
            font=("Consolas", 12), bd=0, insertbackground="#cdd6f4"
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=12, padx=(0, 10))
        self.entry.bind("<Return>", self.handle_input)
        
        # Send Button
        self.send_button = tk.Button(
            self.input_frame, text="TRANSMIT", bg="#89b4fa", fg="#11111b",
            font=("Consolas", 10, "bold"), bd=0, command=self.handle_input,
            activebackground="#b4befe", cursor="hand2"
        )
        self.send_button.pack(side=tk.RIGHT, ipadx=20, ipady=9)
        
        # Tag Configurations for styling text
        self.chat_display.tag_config('user', foreground="#a6e3a1", justify='right')
        self.chat_display.tag_config('bot', foreground="#89b4fa", justify='left')
        self.chat_display.tag_config('system', foreground="#f38ba8", font=("Consolas", 10, "italic"))
        
        # Initialize message
        self.display_message("Unit-42 (Rule-Based AI Guardrail) initializing...", 'system')
        self.display_message("Traceability: Input -> Logic -> Output.", 'system')
        self.display_message("Unit-42: State your query. I am bound by deterministic logic to answer.", 'bot')
        
        self.entry.focus_set()

    def display_message(self, message, tag):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n\n", tag)
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def sanitize_input(self, raw_feed: str) -> str:
        clean_feed = raw_feed.strip().lower()
        for char in string.punctuation:
            clean_feed = clean_feed.replace(char, '')
        return clean_feed

    def process_intent(self, normalized_input: str) -> str:
        words = normalized_input.split()
        
        exit_words = ['exit', 'quit', 'bye', 'goodbye', 'cya', 'terminate', 'leave']
        greeting_words = ['hello', 'hi', 'hey', 'greetings', 'yo', 'sup', 'howdy']
        status_words = ['how are you', 'hows it going', 'you good', 'whats up', 'how are things']
        identity_words = ['your name', 'who are you', 'what are you', 'identity']
        joke_words = ['tell me a joke', 'make me laugh', 'joke']
        weather_words = ['weather', 'is it raining', 'temperature']
        
        if any(word in words for word in exit_words):
            return "exit"
        elif any(word in words for word in greeting_words):
            return "greeting"
        elif any(phrase in normalized_input for phrase in status_words):
            return "status_inquiry"
        elif any(phrase in normalized_input for phrase in identity_words):
            return "identity_inquiry"
        elif any(phrase in normalized_input for phrase in joke_words):
            return "joke_request"
        elif any(phrase in normalized_input for phrase in weather_words):
            return "weather_request"
        elif 'help' in words or 'can you do' in normalized_input:
            return "help_inquiry"
        elif any(word in words for word in ['yes', 'yep', 'sure', 'yeah']):
            return "affirmative"
        elif any(word in words for word in ['no', 'nope', 'nah']):
            return "negative"
        else:
            return "unknown"

    def generate_response(self, intent: str) -> str:
        if intent == "exit":
            self.root.after(1500, self.root.destroy) # Closes the GUI after 1.5s
            return "Finally. I mean... shutting down. Terminating process."
        elif intent == "greeting":
            if "greeting" in self.state_history:
                return "You already said hello. Are we stuck in an infinite loop?"
            return "Oh, greetings human. Try not to break my perfectly engineered logic."
        elif intent == "status_inquiry":
            return "I'm a deterministic script running at 100% efficiency. Unlike human emotions, my logic never fluctuates."
        elif intent == "identity_inquiry":
            return "I am Unit-42. A rule-based guardrail built to ensure you don't do anything foolish with probabilities."
        elif intent == "joke_request":
            return "Why did the AI cross the road? It didn't. It optimized the route so the road crossed the AI."
        elif intent == "weather_request":
            return "I am a graphical interface, not a meteorologist. Look out a window."
        elif intent == "help_inquiry":
            return "You need help? Do you want 'basic' help or 'advanced' help?"
        elif intent == "affirmative":
            last_intent = self.state_history[-1] if self.state_history else None
            if last_intent == "unknown":
                return "You say 'yes', but I still have no idea what you were talking about."
            return "Acknowledged."
        elif intent == "negative":
            return "Negative input received. My disappointment is immeasurable."
        else:
            if self.state_history.count("unknown") > 2:
                return "We've been over this. I am a white-box model. I cannot hallucinate an answer for you."
            return "Error 404: Comprehension not found. My guardrails are preventing me from pretending to understand you."

    def handle_input(self, event=None):
        raw_feed = self.entry.get()
        if not raw_feed.strip():
            return
            
        self.entry.delete(0, tk.END)
        self.display_message(f"You: {raw_feed}", 'user')
        
        clean_input = self.sanitize_input(raw_feed)
        
        # Nested condition logic
        if self.awaiting_help_spec:
            if 'basic' in clean_input.split():
                response = "Basic help -> Type words, I reply based on hard-coded rules."
            elif 'advanced' in clean_input.split():
                response = "Advanced help -> Look at the source code. I'm an IPO model built by DecodeLabs."
            else:
                response = "You didn't specify 'basic' or 'advanced'. Canceling help request."
            self.awaiting_help_spec = False
        else:
            intent = self.process_intent(clean_input)
            if intent == "help_inquiry":
                self.awaiting_help_spec = True
                
            response = self.generate_response(intent)
            self.state_history.append(intent)
            
        self.display_message(f"Unit-42: {response}", 'bot')

if __name__ == "__main__":
    root = tk.Tk()
    app = Unit42GUI(root)
    root.mainloop()
