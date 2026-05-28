def shutdown(option):

    if option == "Yes":
        return "Shutting down"

    elif option == "No":
        return "Abort shut down"

    else:
        return "Sorry"


user_input = input("Enter Yes or No: ")

print(shutdown(user_input))