# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python

def alphanumeric(password):
	import re
	return re.fullmatch("[a-zA-Z0-9]+", password) is not None
