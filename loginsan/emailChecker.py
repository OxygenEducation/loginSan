#!/usr/bin/env python3
#coding:utf-8


import requests
from validate_email import validate_email


class emailChecker(object):
	""" This class contains methods check email availability. """
	
	
	def checkEmail(email):
		api_key = open('IIRE.key', 'r').readline()
		email_address = str(email)
		response = requests.get(
    				"https://isitarealemail.com/api/email/validate",
    				params = {'email': email_address},
    				headers = {'Authorization': "Bearer " + api_key })

		status = response.json()['status']
		if status == "valid":
			return True
		else:
			return False