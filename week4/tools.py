from langchain.tools import tool

@tool
def navigate_to(url: str):
    """Open a website."""
    print(f"Navigating to {url}")
    return f"Opened {url}"

@tool
def click_element(selector: str):
    """Click an element."""
    print(f"Clicking {selector}")
    return f"Clicked {selector}"

@tool
def type_text(selector: str, text: str):
    """Type text into an element."""
    print(f"Typing '{text}' into {selector}")
    return f"Typed {text}"