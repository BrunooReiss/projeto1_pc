import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital Inicial: '))
aporte  = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses):'))
cdi_anual = float(input('CDI anual (%)'))/100
perc_cdb = float(input('Percentual do CDI (%)'))/100
perc_lci = float(input('Percentual do LCI (%)'))/100
taxa_fii = float(input('Rentabilidade mensal FII (%)'))/100
meta = float(input('meta financeira (R$) '))

#CONVERSÃO CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) -1

#TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupanca = 0.005
montante_poupanca =  (capital * math.pow((1 + taxa_poupanca), meses) + (aporte * meses))

#FII - SIMULAÇOES
#Conferir valores a baixo com o professor
simulacoes_fii = []

valor_final = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))

variacao1 = random.uniform(-0.03, 0.03)
aplicacao1 = valor_final * (1 + variacao1)
simulacoes_fii.append(aplicacao1)

variacao2 = random.uniform(-0.03, 0.03)
aplicacao2 = valor_final * (1 + variacao2)
simulacoes_fii.append(aplicacao2)

variacao3 = random.uniform(-0.03, 0.03)
aplicacao3 = valor_final * (1 + variacao3)
simulacoes_fii.append(aplicacao3)

variacao4 = random.uniform(-0.03, 0.03)
aplicacao4 = valor_final * (1 + variacao4)
simulacoes_fii.append(aplicacao4)

variacao5 = random.uniform(-0.03, 0.03)
aplicacao5 = valor_final * (1 + variacao5)
simulacoes_fii.append(aplicacao5)
media_fii = statistics.mean(simulacoes_fii)
mediana_fii = statistics.median(simulacoes_fii)
desvio_fii = statistics.stdev(simulacoes_fii)
montante_fii = media_fii

#Foramatação Monetaria
print('cdb', locale.currency(montante_cdb, grouping=True))
print('lci', locale.currency(montante_lci, grouping=True))
print('poupanca', locale.currency(montante_poupanca, grouping=True))
print('fii', locale.currency(montante_fii, grouping=True))

#Data de Resgate
data_simulacao = datetime.date.today()
data_resgate = data_simulacao + datetime.timedelta(days=meses*30)
data_ptbr  = data_simulacao.strftime('%d/%m/%Y')
data_ptbr2 = data_resgate.strftime('%d/%m/%Y')

#Execução do prompt
print('\nSIMULADOR DE INVESTIMENTOS')
print('Data da Simulação', data_ptbr)
print('Data de Resgate', data_ptbr2)
print('\nTotal Investido', total_investido)

#Grafico feito apartir do codigo (CTRL + 219)
blocos_cdb = int(montante_cdb_liquido / 1000)
grafico_cdb = '█' * blocos_cdb
print('CDB:', locale.currency(montante_cdb_liquido, grouping=True))
print(grafico_cdb)
blocos_lci = int(montante_lci / 1000)
grafico_lci = '█' * blocos_lci
print('LCI:', locale.currency(montante_lci, grouping=True))
print(grafico_lci)
blocos_poupanca = int(montante_poupanca / 1000)
grafico_poupanca = '█' * blocos_poupanca
print('Poupança:', locale.currency(montante_poupanca, grouping=True))
print(grafico_poupanca)
blocos_fii = int(montante_fii / 1000)
grafico_fii = '█' * blocos_fii
print('FII:', locale.currency(montante_fii, grouping=True))
print(grafico_fii)
print('\nMediana FII:', locale.currency(mediana_fii, grouping=True))
print('Desvio padrão FII:', locale.currency(desvio_fii, grouping=True))
meta = float(input('meta financeira (R$) '))
meta_atingida = montante_fii >= meta
print('Meta atingida:', meta_atingida)