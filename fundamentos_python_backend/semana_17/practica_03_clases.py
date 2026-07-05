class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()

user1 = User("Miguel", "Lmigue@mail.com", "Luissd")
print(user1._email)
print(user1.clean_email())
