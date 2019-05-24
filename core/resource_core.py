from json import dumps
from flask import Response

class BaseResource(object):
	def make_response(self, response, code, header=None):
		response = dumps(response)
		final_response = Response(response, status=code, mimetype='application/json')

		if header:
			for key, value in header.items():
				final_response.headers[key] = value

		return final_response