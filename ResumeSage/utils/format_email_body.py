import re

def format_message(message):
    message = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", message)
    message = re.sub(r"#(\S+)", r"<strong>\1</strong>", message)
    email_body = f"""
    <html>
    <body>
        <p>{message}</p>
    </body>
    </html>
    """
    return email_body

