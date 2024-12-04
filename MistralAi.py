from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from Filter import extract_code_block as fil

api_key = "YUN17aikwehU6AxvZSx1pKnKt8fk5R7S"
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)



def mistral(query:str):

    chat_response = client.chat(
    model=model,
    messages=[ChatMessage(role="user", content=query )]
        )
    
    return chat_response.choices[0].message.content


# print(exec(fil(mistral("open youtube and whatsapp    just write python code only to execute in my system "
#                                  +"you can make simple code like this example webbrowser.open(https://www.youtube.com/results?search_query=naruto)"))))

if __name__=="__main__":
    while 1:

            q=input("eneter you're query")
            print(mistral(q))