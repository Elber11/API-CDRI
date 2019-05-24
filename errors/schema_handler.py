class SchemaErrorHandler(object):
	def __init__(self, msg):
		self.msg = str(msg)
		# print(self.msg)

	def response(self, default=True):
		msg =  """Ocurrio un error al guardar los datos, recuerda que no debes repetir las claves primarias (id) además esta entidad esta asociado con otra(s) entidades de esta api, asi que  tienes que asegurarte que los datos que intentas guardar existan en la otra entidad"""
		if default:
			return {'Error' : msg}, 400
		else:
			return {'Error' : self.msg}, 400