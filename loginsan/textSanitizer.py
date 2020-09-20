#!/usr/bin/env python3
#coding:utf-8


from string import ascii_lowercase


class textSanitizer(object):
	""" This class contains methods to remove special characters from strings. """
	
	@classmethod
	def text_only(cls, input_str):  # Removes trailing spaces & more
		
		input_str = list(input_str)

		while input_str[0] == ' ':  # Remove the trailing spaces
			input_str.remove(0)
		
		input_str  = ''.join(input_str)

		for char in input_str.lower():  # Remove special chars
			if char not in list(ascii_lowercase):
				input_str = input_str.replace(char, '')
		
		return input_str
