# chatbot/utils.py

def chatbot_reply(message: str) -> str:
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return "Hello! How can I assist you today?"
    elif "order" in msg:
        return "You can track your order by providing your order ID."
    elif "return" in msg:
        return "You can return an item within 7 days of delivery."
    elif "refund" in msg:
        return "Refunds are processed in 5-7 business days."
    else:
        return "Sorry, I didn't understand that. Please try asking differently."
