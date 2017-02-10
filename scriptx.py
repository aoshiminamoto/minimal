#! /usr/bin/env python
#! -*- coding: utf8 -*-

import os
import sys
import string
import sqlite3

''' Criação do arquivo de banco de dados... '''
if os.path.exists("database.sqlite3"):
	os.remove("database.sqlite3")

conn = sqlite3.connect("database.sqlite3")
cursor = conn.cursor()

''' Criando lista de campos só para facilitar esse teste de lógica e composição da tabela '''
field_list = [y+str(x) for x,y in zip(range(0,100),string.ascii_letters.lower()*2)]

try:
	''' Criação da tabela na base de dados... '''
	sql = "create table textex ({0})".format(" text, ".join(field_list))
	cursor.execute(sql)
except (Exception, erro):
	print("Erro ao criar tabela textex na base de dados.")
	sys.exit(0)

try:
	''' finalizando a operação executando os inserts.... '''
	for index in range(0, len(field_list)):
		sql = "insert into textex ({0}, {1}) values ('x', 'x')".format(field_list[index], field_list[len(field_list)-(index+1)])
		cursor.execute(sql)
except (Exception, erro):
	print("Erro ao inserir dados tabela textex.")
	sys.exit(0)

conn.commit()
print("Sucesso!")