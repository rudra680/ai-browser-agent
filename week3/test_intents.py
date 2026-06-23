import json
import time

from parse_intent import parse_intent

commands = [
    "Open github.com",
    "Go to Hacker News",
    "Fill the registration form",
    "Click the login button",
    "Summarize this page",
    "Email this summary",
    "Open OpenAI website",
    "Fill my profile form",
    "Navigate to LinkedIn",
    "Click submit",
    "Fill the form"
]

for command in commands:

    print("\n" + "=" * 60)
    print("COMMAND:")
    print(command)

    result = parse_intent(command)

    print("\nRESULT:")
    print(json.dumps(result, indent=4))

    time.sleep(12)