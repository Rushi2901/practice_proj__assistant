import speech_recognition as sr
import pyttsx3
from Online_scrapper import online_scrapper
from Filter import extract_code_block as filter
from MistralAi import mistral
import requests

api_key="29432b6aa8ce4df1b219443922dc7d75"


engine = pyttsx3.init()
voices = engine.getProperty('voices')

def news(topic=None):

        url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
        # url2 = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
        web=url
        # if topic == None:
        #     web=url
        # else:
        #     web = url2
        response= requests.get(web)
        if  response.status_code==200:
                data = response.json()
                articles=data['articles']

                news_dict={}
                news_dict.clear()
                news_dict = {'headlines': [], 'description': []}

                print(news_dict)                

                for article in articles:
                    headline = article.get('title', 'No Title')
                    description = article.get('description', 'No Description')
                    news_dict['headlines'].append(headline)
                    news_dict['description'].append(description)



                return news_dict
        return None



def speak (text):
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()


if __name__=="__main__":
    speak("initializing  assistant......")
    while True:

        r=sr.Recognizer()

        def processCommand(c):
            QL=c.lower()
            FQ=QL.split(" ")[0]
            print(QL)
            # here is my chromedriver path C:\project\voice assistant\chromedriver-win64\chromedriver.exe"
            if any(word in QL for word in ["open","jarvis","play"]) :
                response=mistral(QL + "just write python code only to execute in my system "
                                 +"you can make simple code like this example webbrowser.open(https://www.youtube.com/results?search_query=naruto)")

                
                code=filter(response)
                print(code)
                exec(code)
            
            elif any(word in QL for word in ["news","headline"]) :
                var=news()
                headline=  var['headlines']
                description = var['description']


                for i in range (len(headline)):
                    print(f"Headline no {i}:- {headline[i]}\n Description:- {description[i]}" )
                if "headline " in QL and "description" in QL:
                    for i in  range(len(headline)):
                         speak(f"headline number {i}  {headline[i]} and description of this {description["are not found" if i == None else i]}")
                elif "headline " in QL :
                    speak(headline)
                

            else:
                web=online_scrapper(QL)
                if web is not  None:
                    print(web)
                    speak(web)
                    
                else:
                    AI_chat=mistral(QL)
                    print(AI_chat)
                    speak(AI_chat)



        try:
                
                with sr.Microphone() as source :
                    print("Listening for wakeup word.....")
                   
                    audio= r.listen(source)

                word=r.recognize_google(audio)
                print(word)
              

                if "jarvis" in word.lower() :
                    print("jarvis activated")
                    speak("how can i help you")
                    
                    while True:
                    
                        try:

                                with sr.Microphone() as source :

                                    print("Listening for command.....")
                                    audio= r.listen(source,timeout=5,phrase_time_limit=5)

                                    command=r.recognize_google(audio)
                                    print(f"command recognized:- {command}")

                                
                                    if  "stop" in command.lower() or "end " in command.lower():
                                        
                                        speak("Assistant is closing,goodbye")
                                        break
                                    
                                    else:
                                    
                                        processCommand(command)
                        except sr.UnknownValueError:
                            print("Could not understand audio")
                        except sr.RequestError as e:
                            print(f"Could not request results; {e}")
                        except Exception as e:
                            print(f"An error occurred: {e}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


