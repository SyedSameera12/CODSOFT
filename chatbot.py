def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can i assist you today?"
    elif "how are you" in user_input.lower():
        return "i'm just a computer program , but i'm functioning well. Thank you for asking!" 
    elif "weather" in user_input.lower():
        return "i'm sorry,i am not able to provide weather information at the moment."
    elif "goodbye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "i'm sorry, i don't understand that. Can you please rephrase or ask something else?"
    #Example usage:
    while True:
        user_input = input("you:") 
        if user_input.lower()=='exit':
            print("chatbot:Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            print("chatbot:",chatbot_response)
