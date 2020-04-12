from command import Command

class Youtube(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'http://www.youtube.com/results?search_query={0}&search_type=&aq=-1&oq='.format(arg) 
        else:
            return 'http://www.youtube.com'

    def get_keywords(self):
        return [
            "yt",
            "youtube",
            "tube"
        ]

    def get_description(self):
        return "Searches Youtube"
