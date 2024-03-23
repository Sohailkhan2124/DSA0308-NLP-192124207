import re

text = "Hello, my email is sonu6281sk@gmail.com and my phone number is 628-181-6455."

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

email_match = re.search(email_pattern, text)
phone_match = re.search(phone_pattern, text)

if email_match:
    print("Email found:", email_match.group())
else:
    print("Email not found")

if phone_match:
    print("Phone number found:", phone_match.group())
else:
    print("Phone number not found")
