from command import Command

class Github(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://github.com/search?q={}'.format(arg) 
        else:
            return 'https://github.com'

    def get_keywords(self):
        return [
            "git",
            "github",
            "gh"
        ]

    def get_description(self):
        return "Searches Github"
