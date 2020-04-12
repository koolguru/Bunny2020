from command import Command

class Google(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'http://www.google.com/search?q={0}'.format(arg)
        else:
            return 'http://www.google.com'
    
    def get_keywords(self):
        return [
            "g",
            "google",
            "goog"
        ]

    def get_description(self):
        return "Searches Google"
