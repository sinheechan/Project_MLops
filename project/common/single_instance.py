# -- coding: utf-8 --
class SingletonInstance:
	__instance = None

	@classmethod
	def getinstance(cls):
		return cls.__instance

	@classmethod
	def instance(cls, *args, **kargs) -> object:
		"""

		:rtype: object
		"""
		cls.__instance = cls(*args, **kargs)
		cls.instance = cls.getinstance
		return cls.__instance