class Comment:
    def __init__(self,username,content,likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment("test_user","bonbon",5)
print(comment.username)
print(comment.content)
print(comment.likes)

