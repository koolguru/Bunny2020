from command import Command

class Bing(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://www.bing.com/search?q={}'.format(arg)
        else:
            return 'http://www.bing.com'
    
    def get_keywords(self):
        return [
            "b",
            "bing",
            "bi"
        ]

    def get_description(self):
        return "Searches Bing"
