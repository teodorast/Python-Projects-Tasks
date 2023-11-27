class Email:
    def __init__(self, sender, receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent=True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
    
final_emails = []
command = input()
while command!="Stop":
    sender,receiver,content=command.split()
    email_information = Email(sender,receiver,content)
    final_emails.append(email_information)
    command=input()
indexes = [int(index) for index in input().split(", ")]

for i in indexes:
    final_emails[i].send()

for current_email in final_emails:
    print(current_email.get_info())
    
        