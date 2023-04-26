import openai


def custom_completion(prompt:str,model_name:str):
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0,
    )
    print(response.choices)
    print(f'response : {response.choices[0].text}')