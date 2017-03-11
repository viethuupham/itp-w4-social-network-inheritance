from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp is None:
            self.timestamp = datetime.now()
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    
    def __str__(self):
        strtime = datetime.strftime(self.timestamp, "%A, %b %e, %Y")
        return '@{} {}: "{}"\n\t{}'.format(
            self.user.first_name,
            self.user.last_name, 
            self.text, strtime)
        


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        super(PicturePost, self).__init__(text, timestamp)
        
    def __str__(self):
        strtime = datetime.strftime(self.timestamp, "%A, %b %e, %Y")
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(
            self.user.first_name,
            self.user.last_name,
            self.text,
            self.image_url,
            strtime) 
    
class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        super(CheckInPost, self).__init__(text, timestamp)
         
    def __str__(self):
        strtime = datetime.strftime(self.timestamp, "%A, %b %e, %Y")
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(
            self.user.first_name,
            self.text, 
            self.latitude, 
            self.longitude, 
            strtime)
     
     
