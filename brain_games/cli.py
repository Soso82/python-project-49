import promt
def welcome_user(name):
	name = promt.string('May I have your name?')
	return f'Hello, {name}'
