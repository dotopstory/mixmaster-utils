from _globals import *
import os
import sys
sys.path.append(os.path.abspath("/home/rojeta/server/python-core"))
from lib import *

if(ps('lgs')):
	print('Finalizando LGS e esperando 2 segundos para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill ' + ps('lgs'));
	time.sleep(2)
	if(ps('lgs') == False):
		print('LGS finalizado.\n')
else:
	print('LGS já está finalizado.\n')

if(ps('gms')):
	print('Finalizando GMS e esperando 2 segundos para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill ' + ps('gms'));
	time.sleep(2)
	if(ps('gms') == False):
		print('GMS finalizado.\n')
else:
	print('GMS já está finalizado.\n')

if(ps('zs1')):
	print('Finalizando ZS1 e esperando 60 segundos para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill ' + ps('zs1'));
	x = 60;
	while(x > 0):
		print('Aguarde ' + str(x) + ' segundo(s)')
		time.sleep(1)
		x = x - 1;		
	if(ps('zs1') == False):
		print('ZS1 finalizado.\n')
else:
	print('ZS1 já está finalizado.\n')