#!/usr/bin/env python3
import collections


class LazpyObject(object):

	def __init__(self, target_class):
		self._target_class = target_class
		# TODO : add args/kwargs
		self._instance = None
		print(self.__dict__)


	def __len__(self):
		print("__len__")
		return self.__getattribute__("__len__")()


	def __iter__(self):
		print('__iter__')
		return self.__getattribute__("__iter__")()


	def __getattr__(self, name):
		print(f'__getattr__({name})')


	def __getattribute__(self, name):
		print(f"Getting name : {name}")

		if object.__getattribute__(self, "_instance") is None:
			object.__setattr__(self, "_instance", object.__getattribute__(self, "_target_class")())
			#self._instance = self._target_class()
		# TODO: fix?
		return getattr(object.__getattribute__(self, "_instance"), name)
