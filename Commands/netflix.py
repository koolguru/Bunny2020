from command import Command

class Netflix(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            args = arg.split(' ', 1)
            if args[0].lower() == 'movies' or args[0].lower() == 'movie':
                return 'https://www.netflix.com/browse/genre/34399'
            if args[0].lower() == 'tv' or args[0].lower() == 'shows':
                return 'https://www.netflix.com/browse/genre/83'
            if args[0].lower() == 'list':
                return 'https://www.netflix.com/browse/my-list'  
            return 'https://www.netflix.com/search?q={0}'.format(arg)
        else:
            return 'https://www.netflix.com/'
    
    def get_keywords(self):
        return [
            "nf",
            "netflix",
            "n",
        ]

    def get_description(self):
        return "Searches Netflix. Type 'netflix movies' to jump to movies, 'netflix tv' for tv and 'netflix list' for your list "