#!/usr/bin/env python

class DotGenerator:

	def _get_tables(self):
		return list()
	def _set_tables(self, value):
		self.__dict__['tables'] = list(value)
	tables = property(_get_tables, _set_tables, None, "the tables list")			

	def _get_links(self):
		return list()
	def _set_links(self, value):
		self.__dict__['links'] = list(value)
	links = property(_get_links, _set_links, None, "the links list")			
	
	def _get_props(self):
		return dict()
	def _set_props(self, value):
		self.__dict__['props'] = dict(value)
	links = property(_get_props, _set_props, None, "the properties of the graph")			
	
	def open_graph(self, out):
		# output to stream
		out.write(unicode('strict digraph "database-schema" {\n'))

	def generate_header(self, out):
		# output to stream
		out.write(unicode('viewport="800,1200,0.75,400,600"\n'))
		out.write(unicode('\n'))
		out.write(unicode('splines=true; overlap=portho; model=subset;\n'))
		out.write(unicode('rankdir=BT // - note LR would affect the record-style to stop the fields stacking\n'))

		

	def generate_legend(self, out):
		# output to stream
		out.write(unicode('/* TODO legend here */\n'))

	def generate_tables(self, out):
		# output to stream
		out.write(unicode('/* TODO tables here */\n'))

	def generate_links(self, out):
		# output to stream
		out.write(unicode('/* TODO links here */\n'))

	def close_graph(self, out):
		# output to stream
		out.write(unicode('}'))

	def generate(self, out):
		# output to stream
		self.open_graph(out)
		self.generate_header(out)
		self.generate_legend(out)
		self.generate_tables(out)
		self.generate_links(out)
		self.close_graph(out)