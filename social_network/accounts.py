
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
    
    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def get_timeline(self):
        timeline_list = []
        for person in self.following:
            for posts in person.posts:
                timeline_list.append(posts)
        
        return sorted(timeline_list, key=lambda post: post.timestamp, reverse=True)

    def follow(self, other):
        self.following.append(other)