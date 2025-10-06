class Comment:
    def __init__(self, username, content, likes=0):
        # non public
        # self._username = username
        # self._content = content
        # self._likes = likes

        self.Username = username  # calls Username.setter
        self.Content = content
        self.Likes = likes

    @property
    def Username(self):
        return self._username

    @Username.setter
    def Username(self, username):
        self._username = username
        

    #  self.username = username  - WRONG
    #  This is wrong because self.username refers to the property itself,
    #  not the internal/protcted value.

    @property
    def Content(self):
        return self._content

    @Content.setter
    def Content(self, content):
        self._content = content

    @property
    def Likes(self):
        return self._likes

    @Likes.setter
    def Likes(self, likes):
        self._likes = likes


comment = Comment("user1", "I like this book")
print(comment.Username)  # calls the Username getter
print(comment.Content)
print(comment.Likes)
