

# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'dado que tengo los operandos "([^"]*)" y "([^"]*)"')
def dado_que_tengo_los_operandos_group1_y_group1(step, num1, num2):
    world.cal= Calculadora()
    world.operando1 = int(num1)
    world.operando2 = int(num2)
    
@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
   world.resultado = world.cal.suma(world.operando1, world.operando2)

@step(u'cuando realizo la resta')
def cuando_realizo_la_resta(step):
	world.resultado = world.cal.resta(world.operando1, world.operando2)

@step(u'cuando realizo la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
	world.resultado = world.cal.multiplicacion(world.operando1, world.operando2)

@step(u'cuando realizo la division')
def cuando_realizo_la_division(step):
    world.resultado = world.cal.division(world.operando1, world.operando2)

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, esperado):
    assert int(esperado) == world.resultado, 'El resultado' + esperado + 'no es' + str(world.resultado)