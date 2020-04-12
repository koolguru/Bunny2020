from flask import request, Flask, render_template, redirect
import wikipedia
from command_utils import build_command_map

app = Flask(__name__)
COMMAND_MAP, COMMAND_LIST = build_command_map()


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/q/')
def route():
	#process the query
	try:
		query = str(request.args.get('query', ''))
		tokenized_query = query.split(' ', 1)
		search_command = tokenized_query[0].lower()
		option_args = None
		if len(tokenized_query) == 2:
			option_args = tokenized_query[1]
	except Exception as e:
		print(e)
		search_command = query
		option_args = None
	
	try:
		if search_command == 'help':
			return render_template('help.html', command_list = COMMAND_LIST)
		url = COMMAND_MAP[search_command](option_args)
		return redirect(url)
	except Exception as e:
		# fallback option is to google search
		print(e)
		return redirect(COMMAND_MAP['g'](option_args))

if __name__ == '__main__':
	app.run()
