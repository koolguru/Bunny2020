from command import Command

class Google(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            return 'https://soundcloud.com/search?q={0}'.format(arg)
        else:
            return 'https://soundcloud.com/'
    
    def get_keywords(self):
        return [
            "soundcloud",
            "sound",
            "scould",
            'scloud'
        ]

    def get_description(self):
        return "Searches Soundcloud"