print('========================================================');
print('           "CALCULO DO TEMPO DE VIAGEM" ');
print('======================================================== \n\n');

qlt = float(input(u'INFORME A DISTANCIA A PERCORRER EM Km:\n>'))
vl = int(input(u'INSFOMRE A VELOCIDADE MEDIA DA VIAGEM EM Km/h:\n>'));
t = qlt / vl
hr = int(t)
m = (hr - t).__abs__()
mnt = int(m * 60)
print('VOCE CHEGARA AO SEU DESTINO EM: %dh:%dm.'%(hr, mnt));
print();
import os
os.system("pause")

