import requests
import pandas as pd
import argparse


class HyperScienceEndpoint(object):
	""" Factory class for HyperScience endpoints """
	BASE_URL = 'https://sales1.demo.hyperscience.com'

	@classmethod
	def url(cls, endpoint, *args, method='GET', **kwargs):
		"""
		Get the fully-qualified URL for a given HyperScience REST endpoint.

		:param endpoint: Must be one of the keys in ENDPOINTS.
		:type endpoint: str
		:param method: The HTTP request method, e.g. "GET".
		:type method: str
		:returns: A fully-qualified REST endpoint (URI).
		:rtype: str
		"""
		ERR_MSG = f'{cls.__class__.__name__} endpoint "{endpoint}" not ' \
				  f'supported at this time.'
		try:
			if cls.ENDPOINTS[endpoint][method] is not None:
				_method_ref = getattr(cls, endpoint)
				return _method_ref(method, *args, **kwargs)
		except KeyError:
			raise ValueError(ERR_MSG)
		except:
			raise ValueError(ERR_MSG)
		raise ValueError(ERR_MSG)

	@classmethod
	def submissions(cls, method, *args, submission_id=None, **kwargs):
		_url = 'api/v5/submissions'
		if method.upper() in ['GET']:
			if submission_id is None:
				raise ValueError(
					f"'submission_id' parameter is required."
				)
			return f'{cls.BASE_URL}/{_url}/{submission_id}'

	ENDPOINTS = {
		'submissions': {
			'GET': submissions,
		},
	}


class HyperScienceAPI(object):
	""" Interface with HyperScience REST API """

	@classmethod
	def get_http_headers(cls, token):
		return {'Authorization': f'Token {token}'}

	@classmethod
	def get_data(cls, submission_id, endpoint, token, params=None, **kwargs):
		"""
		Send HTTP GET request to HyperScience REST API.

		:param submission_id: An ID of a HyperScience submission object.
		:type submission_id: int
		:param endpoint: For example: 'sessions'
		:type endpoint: str
		:param token: An authorization token
		:type token: str
		:param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
		:type params: dict | list
		:returns: An HTTP response object.
		:rtype: requests.Response
		"""
		url = HyperScienceEndpoint.url(
			endpoint,
			submission_id=submission_id,
			method_name='GET',
			**kwargs,
		)
		return requests.get(
			url,
			params=params,
			headers=cls.get_http_headers(token),
		)

	@classmethod
	def _parse_submission_header_row(cls, unparsed_data):
		_fields = unparsed_data['documents'][0]['document_fields']
		fields = [f['name'] for f in _fields]
		result = ['submission_id', 'document_id']
		result.extend(fields)
		return result

	@classmethod
	def parse_submission(cls, unparsed_data):
		"""
		Parse a raw submission object from HyperScience.

		:param unparsed_data: A raw submission object returned from HyperScience
		:type unparsed_data: dict
		:returns: A list of rows ready to be written to a CSV file,
			which includes a header row containing field names from the
			submission's documents.  All documents in the submission MUST be
			of the same type, meaning they must use the same HyperScience
			layout.
		:rtype: list
		"""
		if len(unparsed_data['documents']) <= 0:
			return {}
		result = [cls._parse_submission_header_row(unparsed_data)]
		for document in unparsed_data['documents']:
			row = [unparsed_data['id'], document['id']]
			for field in document['document_fields']:
				row.append(field['transcription']['normalized'])
			result.append(row)
		return result


def write_to_csv(data, filename):
	"""
	Write key/value pair data to a CSV file.

	:param data:
	:type data: dict
	:param filename: The fully-qualified filename where
		the CSV file should be written to.
	:type filename: str
	:rtype: None
	"""
	df = pd.DataFrame(data=data[1:], columns=data[0])
	df.to_csv(
		filename,
		index=False,
	)








