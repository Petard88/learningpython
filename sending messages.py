txt_messages = ['hej', 'kurtan!!!', 'ät skit!']
sent_messages= []
def show_messages(messages):
    for txt in messages:
        print(txt)

def send_messages(sendingmsg):
    while txt_messages:
        message = txt_messages.pop()
        print(f"You sent {message} to Kurtan.")
        sent_messages.append(message)



show_messages(txt_messages)
send_messages(txt_messages)

print(txt_messages)
print(sent_messages)