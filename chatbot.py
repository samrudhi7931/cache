import random

# Define a few responses for each type of query
greetings = ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hello! How can I assist you?"]
store_hours = ["Our store is open Monday to Saturday from 9 AM to 9 PM, and on Sundays from 10 AM to 6 PM."]
order_status = ["Please provide your Order ID so I can check the status for you."]
product_availability = ["Let me know the product name, and I’ll check if it's available."]
goodbyes = ["Thank you for visiting! Have a great day!", "Goodbye! Feel free to come back if you need more help."]

# Function to get a random response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return random.choice(greetings)
    elif "hours" in user_input:
        return random.choice(store_hours)
    elif "order" in user_input:
        return random.choice(order_status)
    elif "product" in user_input:
        return random.choice(product_availability)
    elif "bye" in user_input:
        return random.choice(goodbyes)
    else:
        return "I'm here to assist with store hours, order status, and product availability."

# Main chatbot loop
def customer_service_bot():
    print("Welcome to our store support chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        else:
            print(get_response(user_input))

# Run the chatbot
customer_service_bot()

'''Welcome to our store support chatbot! Type 'quit' to exit.
>  Hello
Hello! How can I help you today?
>  how much hours your store is open
Our store is open Monday to Saturday from 9 AM to 9 PM, and on Sundays from 10 AM to 6 PM'''