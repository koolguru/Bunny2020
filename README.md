# Bunny2020
Inspired by Facebook's [bunnylol](https://github.com/ccheever/bunny1) search engine and Jack Yang's
<a href="https://github.com/jackyang127/jack_bunny">jack_bunny</a>, Bunny 2020 is a tool for adding smart and customizable browser shortcuts. 
This version is designed to be a step closer to Facebook's current implementation. Currently, there is a lot of work to be done to deploy and flesh out the shortcuts , but the infrastructure for a complete experience has been built! 

### Commands
List of currently supported commands

* `g [insert query]` searching google
* `spotify [insert class number]` search spotify
* `sound [insert query]` search souncloud
* `youtube [insert query]` search youtube
* `help` returns a list of usable commands

### How to write your own commands
Writing complex and multifaceted commands should be remarkably easy with this implementation! Each command must inherit from the Command class.
Simply add your command in the Commands folder and be sure to rollup all methods to teh get_response method.
