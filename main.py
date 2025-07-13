from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_x_post(user_input: str) -> str:
    payload = {
        "model": "",
        "input": "",
    }

    response = request.post(
        "https://api.openai.com/v1/responses",
        json={},
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        },
    )

def main():
    user_input = input("What should the post be about? ")
    x_post = generate_x_post(user_input)
    print("Generated X post:")
    print(x_post)

if __name__ == "__main__":
    main()
