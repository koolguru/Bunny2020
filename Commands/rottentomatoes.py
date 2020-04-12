from command import Command

class RottenTomatoes(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://www.rottentomatoes.com/search?search={0}'.format(arg)
        else:
            return 'https://www.rottentomatoes.com/us/'
    
    def get_keywords(self):
        return [
            "rt",
            "rottentomatoes",
        ]

    def get_description(self):
        return "Search Rotten Tomatoes"
