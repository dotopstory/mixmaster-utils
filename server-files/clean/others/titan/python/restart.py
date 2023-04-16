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

_continue = False;

if(runServerPartWhitoutOutput("lgs")):
	print('Esperando 5 segundos para ver se o LGS inciou.\n')
	time.sleep(5);
	result = ps("lgs")
	if(result):
		print('O LGS foi iniciado.\n')
		_continue = True;
	else:	
		_continue = False;
		print('Falha ao iniciar o LGS. Confira se tudo está correto em /home/rojeta/server/' + GLOBAL_SERVER + '/lgs/lgs.cfg e ftplist.cfg\n')
else:
	_continue = True;
	print('O LGS já está iniciado.\n')

if(_continue):
	if(runServerPartWhitoutOutput("gms")):
		print('Esperando 5 segundos para ver se o GMS inciou.\n')
		time.sleep(5);
		result = ps("gms")
		if(result):
			print('O GMS foi iniciado.\n')
			_continue = True;
		else:	
			_continue = False;
			print('Falha ao iniciar o GMS. Confira se tudo está correto em /home/rojeta/server/' + GLOBAL_SERVER + '/gms/gms.cfg e zsgate.cfg\n')
	else:
		_continue = True;
		print('O GMS já está iniciado.\n')
else:
	print('Como houve uma falha ao iniciar umas das partes do servidor. Iremos finalizar todos os processos do servidor.')
	instantKill()

if(_continue):
	if(runServerPartWhitoutOutput("zs1")):
		print('Esperando 10 segundos para ver se o ZS1 inciou.\n')
		time.sleep(10);
		result = ps("zs1")
		if(result):
			print('O ZS1 foi iniciado.\n')
			_continue = True;
		else:	
			_continue = False;
			print('Falha ao iniciar o ZS1. Confira se tudo está correto em /home/rojeta/server/' + GLOBAL_SERVER + '/zs1/zs.cfg\n')
	else:
		_continue = True;
		print('O ZS1 já está iniciado.\n')
else:
	print('Como houve uma falha ao iniciar umas das partes do servidor. Iremos finalizar todos os processos do servidor.')
	instantKill()


if(_continue == False):
	print('Como houve uma falha ao iniciar umas das partes do servidor. Iremos finalizar todos os processos do servidor.')
	instantKill()