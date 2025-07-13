from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_x_post(topic: str) -> str:
    prompt = f"""
        You are an expert social media manager, and you excel at crafting viral and highly engaging posts for the X platform (formerly Twitter).

        Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.

        Avoid using hashtags and lost of emojis (a few emojis are okay, but not too many).

        Keep the post short and focused, structure it in a clean, readable way using linebreaks and empty lines to enhance readability.

        Here's the topic provided by the user for which to need to generate a post:
        <topic>
            {topic}
        </topic>
    """

    payload = {
        "model": "gpt-4o",
        "input": prompt,
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
