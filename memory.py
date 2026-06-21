import json
import asyncio

async def read_user():
    with open("user.json", "r") as file:
        data = json.load(file)

    print("Name:", data["name"])
    print("Email:", data["email"])
    print("Phone:", data["phone"])
    print("Address:", data["address"])

asyncio.run(read_user())