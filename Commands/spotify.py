from command import Command

class Google(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://open.spotify.com/search/{0}'.format(arg)
        else:
            return 'http://open.spotify.com'
    
    def get_keywords(self):
        return [
            "spotify",
            "spoti",
        ]

    def get_description(self):
        return "Searches Spotify"
