from openai import OpenAI


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

    print(completion.choices[0].message)


def generate_image(user_prompt="A peaceful sea."):
    client = OpenAI()

    response = client.images.generate(
        prompt=user_prompt,
        n=2,
        size="1024x1024"
    )

    print(response.data[0].url)