import random

#responses
responses={
    "hello":["hello,how are you","heyy good morning!!","hii"],

    "how are you":["i am good.","i am doing great!"],
    "goodbye":["byee,have a nice day...","see you take care."],
    "i need to talk about my mental health":["sure,how can I help you?\ndo you feel depressed or anxious? "],
    "anxious":["it's importanat to take care of your mental health."],
    "depressed":["did you consult any specialist about it?"],
    "thank you":["you're welcome...","haave a great day"],
    "default":["i'm sorry i don't get your question","can you repeat?"]

}

def generate_response(input_text):
    input_text=input_text.lower()
    if "hello"  in input_text:
        return random.choice(responses["hello"])
    elif "how are you" in input_text:
        return random.choice(responses["how are you"])
    elif "i need to talk about my mental health" in input_text:
        return random.choice(responses["i need to talk about my mental health"])
    elif "anxious" in input_text:
        return random.choice(responses["anxious0"])
    elif "depressed" in input_text:
        return random.choice(responses["depressed"])
    elif "goodbye" in input_text:
        return random.choice(responses["goodbye"])
    elif "thank you" in input_text:
        return random.choice(responses["thank you"])
    else:
        return random.choice(responses["default"])
    
def main():
    print("Welcome to  MentalHealthMattersBot, how can I help you?")
    while True:
        user_input=input("You:")
        if user_input.lower()=="quit":
            print(random.choice(responses["goodbye"]))
            break
        response =generate_response(user_input)
        print("MentalheathMatters:"+response)

if __name__=='__main__':
        main()
