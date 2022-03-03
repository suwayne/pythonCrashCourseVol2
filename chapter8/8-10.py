messages = [
    "i'm on pcc chapter8",
    "coding is addictive",
    "lets crush what's left",
]
sent_messages = []


def send_messages(messages, sent_messages):
    """
    simulate printing each message, until none are left.
    move each message to sent_messages.
    """
    print("\nThe following messages have been printed:")
    while messages:
        moved_messages = messages.pop()
        print(f"Sent messages: {moved_messages}")
        sent_messages.append(moved_messages)


send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
