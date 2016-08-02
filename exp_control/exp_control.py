#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exp_control.py
#
#  Copyright 2016 Eduard Pinuaga Linares <info@did-web.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import sys

class AuthException(Exception):

	def __init__(self):
		super(AuthException, self).__init__()




class UserNotExist(AuthException):
	def __str__(self):
		return "Usuario No existe"

class PasswordNotCorrect(AuthException):
	def __str__(self):
		return "Password incorrecto"


class DobleRegistro(AuthException):
	def __str__(self):
		return "Se ha intentado registrar 2 veces. [Debe hacer LogOut]"


class LoginIsFalse(AuthException):
	def __str__(self):
		return "No puede hacer LogOut sin Logearse antes."


class ErrorConfig(AuthException):
	def __str__(self,variable):
		return variable," No es una opción valida."


