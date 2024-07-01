class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")
emails = []

while True:
    line = input()
    if line == 'Stop':
        break
    sender, receiver, content = line.split(' ')
    email = Email(sender, receiver, content)
    emails.append(email)

sent_indexes = list(map(int, input().split(', ')))

for idx in sent_indexes:
    emails[idx].send()

for email in emails:
    email.get_info()