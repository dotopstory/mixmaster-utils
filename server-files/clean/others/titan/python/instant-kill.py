from _globals import *
import os
import sys
sys.path.append(os.path.abspath("/home/rojeta/server/python-core"))
from lib import *

if(ps('lgs')):
	print('Finalizando LGS e esperando 1 segundo para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill -9 ' + ps('lgs'));
	time.sleep(1)
	if(ps('lgs') == False):
		print('LGS finalizado.\n')
else:
	print('LGS já está finalizado.\n')

if(ps('gms')):
	print('Finalizando GMS e esperando 1 segundo para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill -9 ' + ps('gms'));
	time.sleep(1)
	if(ps('gms') == False):
		print('GMS finalizado.\n')
else:
	print('GMS já está finalizado.\n')

if(ps('zs1')):
	print('Finalizando ZS1 e esperando 1 segundo para ver se foi finalizado.\n')
	runProgramWithoutOutput('kill -9 ' + ps('zs1'));
	time.sleep(1)		
	if(ps('zs1') == False):
		print('ZS1 finalizado.\n')
else:
	print('ZS1 já está finalizado.\n')