#!/usr/bin/env python
#coding=utf-8

#el juego del numero version python
#4 y 5 de enero de 2007 - Martin Gaitan
#bajo licencia GPL v2 o superior

#gaitan@gmail.com 

"""El Numero es un juego de logica y habilidad mental. 
  Consiste en encontrar el numero escondido (generado aleatoriamente) a traves de la informacion 
  que brinda el juego en cada intento. El numero escondido tiene 4 cifras no repetidas.
  Un digito 'bien' significa que el hay un acierto en numero y peso. 
  Un digito 'regular' significa que el digito existe en el numero incognita, pero no esta en 
  la posicion correcta.
  Por ejemplo si el numero incognita fuese el 1234 y arriesga el 2031 tendra dos digitos 'regular' (el 2 y el 1)
  y 1 digito bien (el 3). 
"""
 
import random

def CargarNumero(jugador):	
		while 1:
			cadena = raw_input('Ingresa tu numero (* p/historial):')
			if cadena == "*": 
				jugador.ver_historial()

			elif cadena == "s":
				mi_juego.terminar()


			else:	
				if valido(cadena):
					return cadena
					break
				else:
					print "El numero que ingresaste no es valido, torpe"

def valido(num_manual):
	if not num_manual.isdigit( ) or len(num_manual) != 4:  #compruebo si todos los caracteres son 4 digitos
		return False
	else:
		#compruebo si hay digitos repetidos
		for x in range(4):
			for y in range(x+1, 4):
				if num_manual[x] == num_manual[y]:
					return False
	return True
	
def generar(num_manual):	
	num = []
	for x in num_manual: 
		num.append(int(x))
	return num

def ganador(jugador):
	print "*************************************************"
	print	jugador.nombre + " ha ganado el partido en " + str(jugador.cant_intentos) + " intentos!!!!"
	print	"*************************************************"

	

class Numero:
	def __init__(self, cadena=""):
		#generacion de un numero aleatorio
		if cadena == "":
			self.num = random.sample(range(10),4)
			
		else:
			self.num = generar(cadena)
			

	def __repr__(self):
		return str(self.num[0]) + str(self.num[1]) + str(self.num[2]) + str(self.num[3])

	def comparar(self, otro):
		self.bien = 0
		self.regular = 0
		for x in range(4):
			for y in range(4):
				if self.num[x] == otro.num[y]:
					if x==y: 
						self.bien = self.bien + 1
					else:
						self.regular = self.regular + 1
		return [self.bien, self.regular]



	
class Jugador:
	def __init__(self):
		
		self.nombre = raw_input("Nombre del jugador?")
		self.incognita = Numero()
		self.cant_intentos = 0
		self.intentos = []
		self.resultados = []
		#self.inicio = time.time()
		self.tiempo = 0
	
	def	ver_historial(self):
		print "#\t Numero\t Bien\t Regular"
		print "---------------------------------"
		for x in range(self.cant_intentos - 1):
			print str(x + 1) + "\t " + str(self.intentos[x]) + "\t " + str(self.resultados[x][0]) + "\t " + str(self.resultados[x][1])
			
		
	
		
	def __repr__(self):
		print "=================================="
		print "Nombre: " + self.nombre
		print "Intentos: " + str(self.cant_intentos)
		#print "Hora de inicio" + gmtime(self.inicio)
		print "=================================="
		
	
		
class Juego:
	def	__init__(self):
		#inicializo jugadores
		while 1:
			entrada = raw_input("Cuantos jugadores? (1 por defecto)")
			if entrada.isdigit() or entrada=="":
				if entrada=="" or int(entrada) <= 1 or int(entrada) > 99 :
					self.cant_jugadores = 1
					print "inicializando 1 jugador..." 
				else:
					self.cant_jugadores = int(entrada)	
					print "inicializando " + entrada + " jugadores..." 
				break	
			else:
				print "por favor ingresa un numero valido, salame"
				
		
		self.jugadores = []
		for x in range(self.cant_jugadores):
			self.jugadores.append(Jugador())
			
		
	def	jugar(self):
		turno = 0
		while 1:
			# verifico que el turno no exceda la cantidad de jugadores
			if turno == self.cant_jugadores:
				turno = 0
			
			self.jugadores[turno].cant_intentos = self.jugadores[turno].cant_intentos + 1
			if turno == 0: 
				#imprimo un cartel una vez por ronda
				print "Intento # " + str(self.jugadores[turno].cant_intentos)
				print "==========================================="
			
			print "Juega " + self.jugadores[turno].nombre 
			
			#cargo el numero del jugador. el numero se pide tantas veces hasta que sea valido. 
			
			mi_numero = Numero(CargarNumero(self.jugadores[turno]))
			
			#depuracion
			#print mi_numero
			
			#guardo el numero en el historial del jugador
			self.jugadores[turno].intentos.append(mi_numero)
			
			#comparo el numero ingresado por el jugador y lo almaceno en la pila de su historial
			result = self.jugadores[turno].incognita.comparar(mi_numero)
			self.jugadores[turno].resultados.append(result)
			
			#gano el juego??
			if result==[4, 0]:
				ganador(self.jugadores[turno])
				self.resultados()
	
				break					#fin del juego
			else:
				#muestro los resultados
				print "BIEN: " + str(result[0])
				print "REGULAR " + str(result[1])
				print "----------------------------------------------"
				turno = turno + 1  		#cedo el turno al siguiente jugador

		
	def resultados(self):
		#imprimo los resultados
		for x in self.jugadores:
			print "numero de " + x.nombre + " = " + x.incognita 
	def terminar(self):
		self.resultados()
		print "chau cobarde(s)"
		
#pruebas...
mi_juego = Juego()

#alla vamos!
mi_juego.jugar()
