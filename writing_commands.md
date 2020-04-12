# Writing Your Own Shortcuts

### A Brief Word About Design
A key facet of Bunny2020 is that shortcut definitions and the core Bunny2020 code are decoupled. 
When you add a shortcut, Bunny2020 will automatically build a mapping from keyword to function. 
The end result is that you should not have to edit any files aside from your own shortcut!

### Defining a Shortcut
A shortcut is simply a python class that inherits from the command class. Each command needs to implement the methods
`get_response`, `get_keywords`, and `get_description`. Beyond this a shortcut can use any functionality available in Python. 
Just remember to make sure to call those methods in get_response!

You can define a simple shortcut like this

```python
from command import Command

class Google(Command):
    
    def __init__(self):
        super()
        return
    
    def get_response(self, arg=None):
        ## Return the URL to go to here 
        if arg:
            return 'http://www.google.com/search?q={0}'.format(arg)
        else:
            return 'http://www.google.com'
    
    def get_keywords(self):
        ## Define as many keywords as you want!
        return [
            "g",
            "google",
            "goog"
        ]

    def get_description(self):
        ## Help others understand your shortcut!
        return "Searches Google"
``` 

Note: arg is a string containing everything in the query after the keyword. This means you can add aditional logic based on the contents of arg 

