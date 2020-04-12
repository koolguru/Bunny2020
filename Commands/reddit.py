from command import Command

class Reddit(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        if arg:
            args = arg.split(' ', 1)
            if len(args) < 2:
                args.append('')
            if args[0].lower() == 'r':
                return 'https://www.reddit.com/r/{}'.format(args[1])
            return 'https://www.reddit.com/search/?q={0}'.format(arg)
        else:
            return 'https://www.reddit.com/'
    
    def get_keywords(self):
        return [
            "r",
            "rd",
            "reddit",
        ]

    def get_description(self):
        return "Searches reddit"