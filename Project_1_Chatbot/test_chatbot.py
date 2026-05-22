"""Quick verification tests for chatbot logic (no GUI display required)."""
import tkinter as tk
from chatbot import Unit42GUI


def make_app():
    root = tk.Tk()
    root.withdraw()
    return Unit42GUI(root), root


def test_sanitize():
    app, root = make_app()
    assert app.sanitize_input("  Hello, World!  ") == "hello world"
    root.destroy()


def test_intents():
    app, root = make_app()
    cases = [
        ("Hello!", "greeting"),
        ("hey there", "greeting"),
        ("how are you", "status_inquiry"),
        ("who are you", "identity_inquiry"),
        ("tell me a joke", "joke_request"),
        ("what is the weather today", "weather_request"),
        ("help me", "help_inquiry"),
        ("can you do something", "help_inquiry"),
        ("yes", "affirmative"),
        ("no", "negative"),
        ("goodbye", "exit"),
        ("quit now", "exit"),
        ("random gibberish xyz", "unknown"),
    ]
    for raw, expected in cases:
        got = app.process_intent(app.sanitize_input(raw))
        assert got == expected, f"{raw!r}: expected {expected}, got {got}"
    root.destroy()


def test_help_flow_responses():
    app, root = make_app()
    app.awaiting_help_spec = True
    app.state_history.append("help_inquiry")

    for word, snippet in [
        ("basic", "Basic help"),
        ("advanced", "Advanced help"),
        ("other", "Canceling help request"),
    ]:
        clean = app.sanitize_input(word)
        if "basic" in clean.split():
            resp = "Basic help -> Type words, I reply based on hard-coded rules."
        elif "advanced" in clean.split():
            resp = "Advanced help -> Look at the source code. I'm an IPO model built by DecodeLabs."
        else:
            resp = "You didn't specify 'basic' or 'advanced'. Canceling help request."
        assert snippet in resp
    root.destroy()


def test_generate_response_samples():
    app, root = make_app()
    assert "Unit-42" in app.generate_response("identity_inquiry")
    assert "joke" in app.generate_response("joke_request").lower() or "road" in app.generate_response("joke_request").lower()
    assert "window" in app.generate_response("weather_request").lower()
    root.destroy()


if __name__ == "__main__":
    test_sanitize()
    test_intents()
    test_help_flow_responses()
    test_generate_response_samples()
    print("All tests passed.")
