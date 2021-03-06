# Bunny2020
Inspired by Facebook's [bunnylol](https://github.com/ccheever/bunny1) search engine and Jack Yang's
<a href="https://github.com/jackyang127/jack_bunny">jack_bunny</a>, Bunny2020 enables smart, customizable shortcuts accessible from your Browser's address bar. Bunnylol is evolved to be one of the most widely used internal tools at Facebook and has evolved a lot since Charlie Cheever published his original version. This version is designed to be a step closer to Facebook's current implementation which allows for complex shortcuts with unlimited keywords. Of course, Facebook's version is written in PHP. Since I hate PHP, this version leverages Python! Currently, there is a lot of work to be done to deploy and flesh out the shortcuts but the infrastructure for a complete experience has been built! 

### Installation
[Installation](https://github.com/koolguru/Bunny2020/blob/master/INSTALLATION.md)


### Example Commands
Some commands that are currently implemented

* `reddit [insert query]` search reddit
  * `reddit r [insert query]` search sub reddits
* `netflix movies` jump to netflix movies
* `spotify [insert query]` search spotify
* `sound [insert query]` search soundcloud
* `youtube [insert query]` search youtube
* `github  [insert query]` search github
* `g [insert query]` searching google (default)
* `help` returns a list of usable commands

### How to write your own commands
Writing complex and multifaceted commands should be remarkably easy with this implementation! Check out [this guide](https://github.com/koolguru/Bunny2020/blob/master/writing_commands.md) for more details.

### Examples

Typing `spotify kanye` into the address bar leads you to 

![](https://github.com/koolguru/Bunny2020/blob/master/assets/spotify.png?raw=true)
