from openai import OpenAI
from colorama import Fore
import webbrowser


def generate_text(choose_model="gpt-4o-mini", user_input="Randomly tell me something, news, jokes, movie recommendations, or some terminal or computer tricks, just like the start screen of windows."):
    client = OpenAI()

    completion = client.chat.completions.create(
        model=choose_model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    """ content example
        {
    "choices": [
        {
        "finish_reason": "stop",
        "index": 0,
        "message": {
            "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
            "role": "assistant"
        },
        "logprobs": null
        }
    ],
    "created": 1677664795,
    "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
    "model": "gpt-4o-mini",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 17,
        "prompt_tokens": 57,
        "total_tokens": 74
    }
    }
    """

    print(Fore.GREEN + "----------GPT Response-----------")
    print(Fore.GREEN + completion.choices[0].message.content)
    print(Fore.GREEN + "---------------------------------")


def generate_image(user_prompt="A peaceful sea.", display=False):
    client = OpenAI()

    response = client.images.generate(
        prompt=user_prompt,
        n=2,
        size="1024x1024"
    )

    if display == False:
        print(response.data[0].url)
    else:
        webbrowser.open(response.data[0].url)
        

