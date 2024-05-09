from openai import OpenAI

client = OpenAI(api_key='sk-proj-SrjbIu0F1jaeKU4jLHuaT3BlbkFJKalJpMQuYDt9PQgM6')

def Sentiment_analysis(text):
    messages = [
        {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text.
                                         if you are unsure of an answer, you can say "not sure" and recommend users to review manually.""" },
        {"role": "system", "content": f""""Analyse the following text and determine if the sentiment is:positive or negative.
                                                 Return answer in single word as either positive or negative: {text}""" }
    ]
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages=messages,
    max_tokens=1,
    n=1,
    stop=None,
    temperature=0)

    response_text = response.choices[0].message.content.strip().lower()
    return response_text

#calling the function
input = "I love my wife"
response = Sentiment_analysis(input)
print(input, 'THE SENTIMENT IS', response)