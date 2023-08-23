user_message = "--300 chak"
if user_message[:2] == "--":
    for x in user_message:
        if x == " ":            
            last = user_message.index(x)
            str_time = user_message[2:last]
            print(int(str_time))
            print(user_message[last+1:])