import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: '))/100
perc_cdb = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('Rentabilidade do FII (%): '))/100
meta = float(input('Meta financeira (R$): '))

#conversao CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

#total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb),meses))+(aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses))+(aporte * meses)

#FII Simulação Estatística
fii1 = (capital * math.pow((1+taxa_fii), meses))+(aporte * meses) * (1+ random.uniform(-0.03, 0.03))
fii2 = (capital * math.pow((1+taxa_fii), meses))+(aporte * meses) * (1+ random.uniform(-0.03, 0.03))
fii3 = (capital * math.pow((1+taxa_fii), meses))+(aporte * meses) * (1+ random.uniform(-0.03, 0.03))
fii4 = (capital * math.pow((1+taxa_fii), meses))+(aporte * meses) * (1+ random.uniform(-0.03, 0.03))
fii5 = (capital * math.pow((1+taxa_fii), meses))+(aporte * meses) * (1+ random.uniform(-0.03, 0.03))

fii_media = statistics.mean( (fii1, fii2, fii3, fii4, fii5) )
fii_mediana = statistics.median(( fii1, fii2, fii3, fii4, fii5 ))
fii_desvio = statistics.stdev(( fii1, fii2, fii3, fii4, fii5 ))

#DATAS
data_simulacao = datetime.datetime.now()
data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

#META

meta_atingida = (fii_media >= meta)
 
#formatação
capital_fmt = locale.currency(capital, grouping=True)
total_fmt = locale.currency(total_investido, grouping=True)
cdb_fmt = locale.currency(montante_cdb_liquido, grouping=True)
lci_fmt = locale.currency(montante_lci, grouping=True)
poup_fmt = locale.currency(montante_poupanca, grouping=True)
fii_fmt = locale.currency(fii_media, grouping=True)
fii_med_fmt = locale.currency(fii_mediana, grouping=True)
fii_des_fmt = locale.currency(fii_desvio, grouping = True)

#grafico ASCII
graf_cdb = '█' * int(montante_cdb_liquido / 1000)
graf_lci = '█' * int(montante_lci / 1000)
graf_poup = '█' * int(montante_poupanca / 1000)
graf_fii = '█' * int(fii_media / 1000)

print('='*40)
print('-- PyInvesT - Simulador de Investimentos --')
print('-'*40)
print('Data da simulação: ', data_simulacao.strftime('%d/%m/%Y'))
print('Data estimada de resgate:', data_resgate.strftime('%d/%m/%Y'))
print('='*40)

print('\nTotal investido:', total_fmt)

print('\n--- RESULTADOS FINANCEIROS ---')
print('CDB:', cdb_fmt)
print(graf_cdb)

print('LCI/LCA:', lci_fmt)
print(graf_lci)

print('Poupança:', poup_fmt)
print(graf_poup)

print('FII (média):', fii_fmt)
print(graf_fii)

print('\n--- ESTATÍSTICAS FII ---')
print('Mediana:', fii_med_fmt)
print('Desvio padrão:', fii_des_fmt)

print('\nMeta atingida:', meta_atingida)
print('='*40)