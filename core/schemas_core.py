from flask import request
from marshmallow import Schema
from marshmallow import EXCLUDE
from marshmallow import post_load
from sqlalchemy import desc
from sqlalchemy import asc
from marshmallow import ValidationError
from sqlalchemy_filters import apply_filters
from orderdict import order
from flask_jwt_extended import jwt_required

from core.sqlalchemy import db
from constants.limit import previous_limit
from errors.schema_handler import SchemaErrorHandler

class BaseSchemas(Schema):
	class Meta:
		ordered = True

	response = {
					'count' : 0,
					'offset' : 0,
					'limit' : 10,
					'next_page' : '',
					'previous_page' : ''
				}

	@classmethod
	@jwt_required
	def get(cls, get_args=None, id=False, raw_result=False):
		from marshmallow.fields import Nested
		get_args = get_args or dict(request.args.copy())
		exclude = []
		_model = cls()

		for key, value in get_args.items():
				if key == 'fields':
					if not value:
						return {'Bad Request' : 'El campo \'fields\' no puede estar vacio'}, 400

					counter = 0
					only = value.split(',')

					for elem in only:
						try:
							if type(_model.fields[only[counter][:-3]]) == Nested:
								only[counter] = only[counter][:-3]
							counter += 1
						except:
							counter += 1
							continue

					exclude = [elem for elem in list(_model.fields) if elem not in only]
					
					if len(exclude) == len(_model.fields):
						return {'Bad Request' : 'Parece que tienes errores en los campos que quieres filtrar'}, 400

					del get_args['fields']

					break

		_model = cls(exclude=exclude)

		return _model.__get__(get_args=get_args, id=id, raw_result=raw_result)
	
	def __get__(self, get_args=None, id=False, raw_result=False):
		self.many = True
		query = self.__model__.query if not id else self.__model__.query.filter_by(id=id)
		get_args = get_args or dict(request.args.copy())
		response = self.response.copy()
		next_page = request.base_url
		previous_page = request.base_url
		page = 1
		
		if get_args.get('limit'):
			response['limit'] = int(get_args['limit'])

			if not response['limit']:
				response['limit'] = self.response['limit']

			del get_args['limit']

		if get_args.get('offset'):
			response['offset'] = int(get_args['offset'])

			if response['offset'] == 1 or response['offset'] == 2:
				response['offset'] += 0.5

			del get_args['offset']

		page = (response['offset'] / response['limit']) + 1

		if get_args:
			try:
				query = self.add_filters(query, get_args)
			except Exception as msg:
				return {'Bad Request' : str(msg)}, 400

		result = query.paginate(page, response['limit'])

		if len(result.next().items) != 0:
			next_page += self.next_page(result.total, response['offset'], response['limit'], get_args)

		else:
			next_page = ''
 
		if result.has_prev:
			previous_page += self.previous_page(response['offset'], response['limit'], get_args)

		else:
			previous_page = ''

		all_results = result.items
		all_results = self.dump(all_results)

		if not all_results:
			return {'Not Found' : 'No se encontraron resultados'}, 404

		if raw_result:
			return all_results[0], 200

		response['offset'] = int(response['offset'])
		response['count'] = result.total
		response['next_page'] = next_page
		response['previous_page'] = previous_page
		response['data'] = all_results

		return response, 200

	def add_filters(self, query, args):
		filters = []

		for key, value in args.items():
			_filter = {}

			if key == 'order' or key == 'desc' or key == 'asc':
				if key == 'desc' or key == 'asc':
					continue

				if value not in self.__filtering__:
					raise Exception("No se puede ordenar la busqueda por el campo '{value}', no existe.".format(value=value))

				if args.get('desc', False):
					query = query.order_by(desc(value))

				elif args.get('asc', False):
					query = query.order_by(asc(value))
				
				else:
					query = query.order_by(value)

			elif key not in self.__filtering__:
				raise Exception("No se puede filtrar la busqueda por el campo '{key}', está vacío o no existe".format(key=key))

			else:
				_filter['field'] = key
				_filter['op'] = 'like'
				_filter['value'] = '%' + value + '%'
				filters.append(_filter)

		filtered_query = apply_filters(query, filters)

		return filtered_query
		
	def next_page(self, count, offset, limit, args):
		offset = offset + limit
		
		if offset + limit > count:
			previous_limit[0] = limit

		while offset + limit > count:
			limit -= 1

		url = '?offset=' + str(offset) + '&limit=' + str(limit)

		if args:
			for key, value in args.items():
				url += '&{key}={value}'.format(key=key, value=value)

		return url

	def previous_page(self, offset, limit, args):
		if previous_limit[0]:
			limit = previous_limit[0]

		offset = offset - limit
		
		while offset < 0:
			offset += 1

		url = '?offset=' + str(offset) + '&limit=' + str(limit)

		if args:
			for key, value in args.items():
				url += '&{key}={value}'.format(key=key, value=value)

		return url

	@jwt_required
	def post(self, post_args=False, show_url=False):
		args = post_args or dict(request.args.copy())
		response = {}

		for key in args.keys():
			if key in self.fields:
				pass
			else:
				return {'Bad Request' : "No existe el parametro '{key}' para esta entidad".format(key=key)}, 400

		primary_key = self.get_primary_key()

		if not primary_key in args:
			args[primary_key] = self.get_next_id()

		try:
			entity = self.load(args)
		except ValidationError as error:
			return {'Bad Request' : error.messages}, 400
		
		db.session.add(entity)

		try:
			db.session.commit()
		except Exception as msg:
			handler = SchemaErrorHandler(msg)
			return handler.response()

		response['Status'] = 'Success'
		response[primary_key] = args[primary_key]

		if show_url:
			response['url'] = request.base_url + str(args[primary_key]) + '/'

		del args[primary_key]
		_order = list(self.fields)
		_order.insert(0, 'Status')
		_order.insert(1, primary_key)

		if show_url:
			_order.append('url')

		for key, value in args.items():
			response[key] = value

		response = order(_order, response)

		return response, 201

	@jwt_required
	def put(self, args=False, response=True, construct_url=True, show_url=False, patch=False):
		args = args or dict(request.args.copy())
		_response = {}

		if len(args) <= 1:
			return {'Bad Request' : 'Debes mandar los parametros que quieres actualizar y/o el identificador de la entidad'}, 400

		primary_key = self.get_primary_key()

		if not primary_key in args:
			return {'Bad Request' : 'Falta la clave primaria (id) de la entidad para actualizar'}, 400

		for key in args.keys():
			if key in self.fields:
				pass
			else:
				return {'Bad Request' : "No existe el parametro '{key}' para esta entidad".format(key=key)}, 400

		query = self.__model__.query
		query = self.add_filters(query, {primary_key : args[primary_key]})
		entity = query.first()

		if not entity:
			return {'Bad Request' : 'No existe una entidad con ese identificador (id)'}, 400

		entity_to_update = dict(self.dump(entity))

		for key, value in args.items():
			try:
				if value == "" or value.strip() == "":
					args[key] = None
			except:
				continue

		for key, value in args.items():
			try:
				entity_to_update[key] = value
			except Exception:
				msg = 'el parametro \'{key}\' no existe para esta entidad'.format(key=key)
				handler = SchemaErrorHandler(msg)
				return handler.response(default=False)

		if patch:
			partial = tuple([elem for elem in entity_to_update.keys() if elem not in [elem for elem in args.keys()]])

			for key in entity_to_update.copy().keys():
				if key in partial:
					del entity_to_update[key]

		try:
			if patch:
				entity_to_update = self.load(entity_to_update, partial=partial)

			else:
				entity_to_update = self.load(entity_to_update, unknown=EXCLUDE)

		except ValidationError as error:
			return {'Bad Request' : error.messages}, 400
			
		if not patch:
			for elem in self.dump(entity_to_update).keys():
				if elem not in args.keys() and not self.fields[elem].dump_only:
					return {'Bad Request' : 'Faltan parametros'}, 400

		for key, value in self.dump(entity_to_update).copy().items():
			if value == None and args.get(key, False) == None:
				setattr(entity, key, value)

			elif value != None:
				setattr(entity, key, value)

		db.session.add(entity)

		try:
			db.session.commit()
		except Exception as msg:
			handler = SchemaErrorHandler(msg)
			return handler.response()

		if not response:
			return True

		_response['Status'] = 'Success'
		_response[primary_key] = args[primary_key]

		if show_url:
			if not construct_url:
				_response['url'] = request.base_url
			else:
				_response['url'] = request.base_url + str(args[primary_key]) + '/'

		del args[primary_key]
		_order = list(self.fields)
		_order.insert(0, 'Status')
		_order.insert(1, primary_key)

		if show_url:
			_order.append('url')

		for key, value in args.items():
			_response[key] = value

		_response = order(_order, _response)

		return _response, 200

	@jwt_required
	def patch(self, *args, **kwargs):
		return self.put(patch=True,*args,**kwargs)

	@jwt_required
	def partial_delete(self, column_status):
		args = dict(request.args.copy())

		primary_key = self.get_primary_key()

		if not primary_key in args:
			return {'Bad Request' : 'Falta la clave primaria (id) de la entidad para eliminar'}, 400

		args = {primary_key : args[primary_key], column_status : "-1"}

		if self.put(args):
			return  'No Content', 204

	@jwt_required
	def delete(self, args=False):
		args = args or dict(request.args.copy())

		primary_key = self.get_primary_key()

		if not primary_key in args:
			return {'Bad Request' : 'Falta la clave primaria (id) de la entidad para eliminar'}, 400

		query = self.__model__.query
		query = self.add_filters(query, {primary_key : args[primary_key]})
		entity = query.first()
		
		if not entity:
			return {'Bad Request' : 'No existe una entidad con ese identificador (id)'}, 400

		db.session.delete(entity)

		try:
			db.session.commit()
		except Exception as msg:
			handler = SchemaErrorHandler(msg)
			return handler.response(default=False)

		return  'No Content', 204

	@post_load
	def make_object(self, data):
		return self.__model__(**data)

	def get_next_id(self):
		from sqlalchemy import func
		from sqlalchemy import select
		
		primary_key = list(self.__model__.__table__.c)
		result =  db.session.execute(select([func.max(primary_key[0])])).first()[0]

		if not result:
			return 1

		result += 1
		
		return result

	def get_primary_key(self):
		primary_key = list(self.__model__.__table__.c)[0]
		primary_key = str(primary_key)
		index = primary_key.index('.')
		primary_key = primary_key[index+1:]

		return primary_key