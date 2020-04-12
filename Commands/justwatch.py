from command import Command

class JustWatch(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://www.justwatch.com/us/search?q={0}'.format(arg)
        else:
            return 'https://www.justwatch.com/us/'
    
    def get_keywords(self):
        return [
            "stream",
            "canstream",
            "justwatch",
        ]

    def get_description(self):
        return "Find if you can stream something"
