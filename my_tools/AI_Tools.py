from openai import OpenAI
from colorama import Fore
from my_tools.IO_Tools import print_slowly
from my_tools.Encode_Tools import encode_image
import webbrowser
import os
import requests

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
    print_slowly(text=completion.choices[0].message.content, color="green")
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
        

def view_image(url=None, image_path=None, usr_input="View the image, and try to describe it."):
    client = OpenAI()

    if url is not None:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content":[
                        {
                            "type": "text",
                            "text": usr_input
                        },
                        {
                            "type":"image_url",
                            "image_url":{"url": url}
                        }
                    ]
                }
            ],
            max_tokens=300, # no more than 300 words
        )
            
        print_slowly(text=response.choices[0].message.content, color="green")

    else:
        if image_path is not None:
            api_key = os.getenv("OPENAI_API_KEY")

            try:
                base64_image = encode_image(image_path)
            except FileNotFoundError as e:
                print(f"Error: {e}. The file was not found.")
                exit
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            payload = {
                "model": "gpt-4o-mini",
                "messages":[
                    {
                        "role": "user",
                        "content":[
                            {
                                "type":"text",
                                "text":usr_input,
                            },
                            {
                                "type":"image_url",
                                "image_url":{
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens":300
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            # Extract and print the content from the response
            response_json = response.json()
            content = response_json['choices'][0]['message']['content']

            print(Fore.GREEN + "----------GPT Response-----------")
            print_slowly(text=content, color="green")
            print(Fore.GREEN + "---------------------------------")


