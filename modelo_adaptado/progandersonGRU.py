import sys

# Obtém o primeiro argumento da linha de comando
argumento = sys.argv[1]

# Converte o argumento para um inteiro
try:
    valor_inteiro = int(argumento)
except ValueError:
    print("O argumento não é um número inteiro válido.")

import shutil
import os
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import GRU #ADICIONEI
import numpy as np
from datetime import date
import csv
#from folium.plugins import HeatMap
import os
#import folium
import time
import webbrowser
#import branca.colormap as cmp
#from folium.features import DivIcon
#from folium.plugins import FloatImage
from scipy import stats
from sklearn.metrics import r2_score
from datetime import datetime

#KERASTUNER

from tensorflow import keras
from tensorflow.keras import layers
from keras_tuner.tuners import RandomSearch


media1=0
media2=0
media3=0
media4=0
media5=0
media6=0
aux=0
now = datetime.now()
nomelogmedia = now
while(aux<valor_inteiro):
	now = datetime.now()
	name4 = now
	os.mkdir(str(name4))
	caminho_destino = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/' + str(name4))
	log = open('ManDados.txt', 'a')
	log.write("------Manipulação dos dados iniciada em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()


	caminho = r'/home/bianca/Área de Trabalho/MODELO'
	cmh = os.path.join(caminho, 'P20Inf')
	################################################Potreiro 20 Infestado#############################################################
	# load dataset
	dataset1 = read_csv('/home/bianca/Área de Trabalho/MODELO/e1.csv', header=0, index_col=0, delimiter=',')
	values1 = dataset1.values
	# integer encode direction
	encoder = LabelEncoder()

	#Drop NA Values
	values1=values1[~np.isnan(values1).any(axis=1)]

	# ensure all data is float
	values1 = values1.astype('float32')

	real1 = values1[:, -1]

	# normalize features
	scaler = MinMaxScaler()
	scaled1 = scaler.fit_transform(values1)

	scaled1 = DataFrame(scaled1)

	#print(scaled)
	#print(scaled2)
	# split into train and test sets
	values1 = scaled1.values

	#n_train = 24
	n_train = 133
	train1 = values1[:n_train, :]
	test1 = values1[n_train:, :]
	#print(train)
	#print(test)
	# split into input and outputs
	train_X1, train_y1 = train1[:, :-1], train1[:, -1]
	test_X1, test_y1 = test1[:, :-1], test1[:, -1]

	#print(train_X)
	#print(train_y)
	#print(test_X1)
	#print(test_y1)

	# reshape input to be 3D [samples, timesteps, features]
	train_X1 = train_X1.reshape((train_X1.shape[0], 1, train_X1.shape[1]))
	test_X1 = test_X1.reshape((test_X1.shape[0], 1, test_X1.shape[1]))

	#print(train_X)
	#print(train_y)
	#print(test_X)
	#print(test_y)

	#print(train_X1.shape, train_y1.shape, test_X1.shape, test_y1.shape)
	#print(train_X1.shape[1])

	now = datetime.now()
	fim = time.time()
	t1 = fim - inicio
	log = open('ManDados.txt', 'a')
	log.write("------ Manipulação dos dados encerrada em: " + str(now) + "\n\nTempo de execução: " + str(t1) )
	log.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/ManDados.txt')
	shutil.move(caminho_origem, caminho_destino)

	#DEFINIçÃO E TREINAMENTO ModeloOriginal

	now = datetime.now()
	log = open('DefTreinoMO.txt', 'a')
	log.write("------Uniao ModeloOriginal Excecução iniciada em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()

	# design network
	model = Sequential()
	#model.add(LSTM(30, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='tanh', return_sequences = True))#bom para 1 e 2
	#model.add(LSTM(15, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='tanh', return_sequences = True))#bom para 1 e 2
	#model.add(LSTM(7, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='tanh'))


	model.add(GRU(30, input_shape=(train_X1.shape[1], train_X1.shape[2]),	kernel_initializer='normal',  return_sequences = True))#bom para 1 e 2
	model.add(GRU(15, input_shape=(train_X1.shape[1], train_X1.shape[2]),	kernel_initializer='normal'))

	#model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='sigmoid'))
	#model.add(LSTM(10, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='softmax'))
	#model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='softplus'))
	#model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='softsign'))
	#model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='hard_sigmoid'))
	#model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='linear'))
	#model.add(LSTM(10, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='selu'))#bom para 2
	#model.add(LSTM(15, input_shape=(train_X.shape[1], train_X.shape[2]),  kernel_initializer='normal', activation='relu'))#bom para 2

	#model.add(Dense(500, kernel_initializer='normal', activation='tanh'))#para 2 melhorou

	# Hidden - Layers

	#model.add(Dropout(0.3, noise_shape=None, seed=None))
	#model.add(Dense(50, activation = "tanh"))
	#model.add(Dropout(0.2, noise_shape=None, seed=None))
	#model.add(Dense(10, activation = "tanh"))

	model.add(Dense(1, kernel_initializer='normal'))

	#model.compile(loss='mse', optimizer='SGD')
	model.compile(loss='mean_squared_error', optimizer='rmsprop')#mto bom para 1 e 2
	#model.compile(loss='mse', optimizer='Adagrad')#mto bom para 1
	#model.compile(loss='mse', optimizer='Adadelta')#mto bom para 1 e 2
	#model.compile(loss='mse', optimizer='Adam')#mto bom para 1
	#model.compile(loss='mse', optimizer='Adamax')#mto bom para 1
	#model.compile(loss='mse', optimizer='Nadam')
	# fit network
	history = model.fit(train_X1, train_y1, epochs=5000, batch_size=72, validation_data=(test_X1, test_y1), verbose=0, shuffle=False)

	now = datetime.now()
	fim = time.time()
	t2 = fim - inicio
	log = open('DefTreinoMO.txt', 'a')
	log.write("------ Excecução Total encerrada em: " + str(now) + "\n\nTempo de execução: " + str(t2) )
	log.close()


	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/DefTreinoMO.txt')
	shutil.move(caminho_origem, caminho_destino)
	
	#CÁLCULOS SEM KERAS TUNER

	now = datetime.now()
	log = open('CalcSKT.txt', 'a')
	log.write("------Cálculos iniciados em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()


	# make a prediction
	yhat1 = model.predict(test_X1)
	test_X1 = test_X1.reshape((test_X1.shape[0], test_X1.shape[2]))
	# invert scaling for forecast
	inv_yhat1 = concatenate((test_X1, yhat1), axis=1)
	inv_yhat1 = scaler.inverse_transform(inv_yhat1)
	inv_yhat1 = inv_yhat1[:,-1]
	# invert scaling for actual
	test_y1 = test_y1.reshape((len(test_y1), 1))
	inv_y1 = concatenate((test_X1, test_y1), axis=1)
	inv_y1 = scaler.inverse_transform(inv_y1)
	inv_y1 = inv_y1[:,-1]

	#print(model.summary())

	#from ann_visualizer.visualize import ann_viz

	#ann_viz(model, title="My first neural network")

	# calculate RMSE
	rmse = sqrt(mean_squared_error(inv_y1, inv_yhat1))
	desvioAmostralpred1 = np.std(inv_yhat1) #desvio padrão populacional
	varianciaAmostralpred1 = inv_yhat1.var() #variancia populacional

	desvioAmostralreal1 = np.std(inv_y1) #desvio padrão populacional
	varianciaAmostralreal1 = inv_y1.var() #variancia populacional

	slope, intercept, r_value, p_value, std_err = stats.linregress(inv_y1, inv_yhat1)


	coeffs1 = np.polyfit(inv_y1, inv_yhat1, 5)
	p1 = np.poly1d(coeffs1)
	# fit values, and mean
	yhat1 = p1(inv_y1)							  # or [p(z) for z in x]
	ybar1 = np.sum(inv_yhat1)/len(inv_yhat1)		   # or sum(y)/len(y)
	ssreg1 = np.sum((yhat1-ybar1)**2)			   # or sum([ (yihat - ybar)**2 for yihat in yhat])
	sstot1 = np.sum((inv_yhat1 - ybar1)**2)			 # or sum([ (yi - ybar)**2 for yi in y])
	r1 = ssreg1 / sstot1

	now = datetime.now()
	fim = time.time()
	t3 = fim - inicio
	log = open('CalcSKT.txt', 'a')
	log.write("------ Cálculos encerrados em: " + str(now) + "\n\nTempo de execução: " + str(t3) )
	log.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/CalcSKT.txt')
	shutil.move(caminho_origem, caminho_destino)

	from keras.utils import plot_model
	plot_model(model, to_file='model_plot_P20-Infestado.png', show_shapes=True, show_layer_names=True)

	erro = []
	for x in inv_yhat1:
		erro = inv_yhat1 - inv_y1

	#Boxplot
	fig1, ax1 = pyplot.subplots()
	pyplot.boxplot([inv_y1, inv_yhat1, erro], labels=['Real', 'Predito', 'Erro'])
	pyplot.title('P20 - Infestado')
	dpi = fig1.get_dpi()

	# Salva a figura no Google Drive
	pyplot.savefig(f'GBoxP_SKT.png', dpi=dpi*2)

	# Exibe o gráfico na tela


	#Gráfico de Dispersão
	pyplot.scatter(inv_yhat1, inv_y1)
	range = [inv_y1.min(), inv_yhat1.max()]
	pyplot.xlim(left=0)
	pyplot.xlim(right=8000)
	pyplot.ylim(bottom=0)
	pyplot.ylim(top=8000)
	pyplot.plot(range, range, 'red')
	pyplot.title('P20 Infestado - Real x Predito')
	pyplot.ylabel('Real')
	pyplot.xlabel('Predito')
	pyplot.savefig(f'GDisp_SKT.png', dpi=dpi*2)


	pyplot.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/GBoxP_SKT.png')
	shutil.move(caminho_origem, caminho_destino)
	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/GDisp_SKT.png')
	shutil.move(caminho_origem, caminho_destino)

	#print('P20 - Infestado')
	#print("R2 linear", r_value ** 2)
	#print("R2 Polinomial:", r1)
	#print('Test RMSE: %.3f' % rmse)
	#print("Desvio Real", desvioAmostralreal1)
	#print("Variancia Real", varianciaAmostralreal1)
	#print("Desvio Predito", desvioAmostralpred1)
	#print("Variancia Predito", varianciaAmostralpred1)
	#print('Real')
	#print(inv_y1)
	#print('Predito')
	#print(inv_yhat1)

	file = open('Log_SKT.txt', "w")
	file.write('P20 - Infestado' + '\n')
	file.write('Test RMSE:' + '%.3f' % rmse + '\n')
	file.write('R2 linear:' + str(r_value ** 2) + '\n')
	file.write("R2 Polinomial:" + str(r1) + '\r')
	file.write("Desvio Real:" + str(desvioAmostralreal1) + '\n')
	file.write("Variancia Real:" + str(varianciaAmostralreal1) + '\n')
	file.write("Desvio Predito:" + str(desvioAmostralpred1) + '\n')
	file.write("Variancia Predito:" + str(varianciaAmostralpred1) + '\n')
	file.write('Real' + '\n')
	for a in inv_y1:
		file.write(str('%.2f' % a) + ',' + ' ')
	file.write('\n' + 'Predito' + '\n')
	for b in inv_yhat1:
		file.write(str('%.2f' % b) + ',' + ' ')
	file.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/Log_SKT.txt')
	shutil.move(caminho_origem, caminho_destino)

	now = datetime.now()
	log = open('RS.txt', 'a')
	log.write("------Definição KT e Random Search iniciada em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()

	def build_model(hp):
		model = keras.Sequential()
		model.add(layers.GRU(
	    		units=hp.Int("gru_units", min_value=30, max_value=512, step=32),
	  		activation=hp.Choice("gru_activation", ["relu", "tanh"]),
	   		return_sequences=True,
	   		input_shape=(1, 35)
	))
		model.add(layers.GRU(
	    		units=hp.Int("gru_units_1", min_value=15, max_value=512, step=32),
	   		activation=hp.Choice("gru_activation", ["relu", "tanh"])
	))
		if hp.Boolean("dropout"):
	    		model.add(layers.Dropout(rate=0.25))
		model.add(layers.Dense(1, activation="sigmoid"))
		learning_rate = hp.Float("lr", min_value=1e-4, max_value=1e-2, sampling="log")
		model.compile(
	    		optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
	    		loss="binary_crossentropy",
	    		metrics=["accuracy"],
	)
		return model

	tuner = RandomSearch(
	build_model,
	objective="val_accuracy",
	# Adaptação para KT
	max_trials=5,
	executions_per_trial=3,
	directory= "KT",
	project_name="p20_infestado",
	)

	tuner.search_space_summary()

	train_X1 = train_X1.reshape(-1, 1, 35)
	test_X1 = test_X1.reshape(-1, 1, 35)
	tuner.search(train_X1, train_y1, epochs=5, validation_data=(test_X1, test_y1))
	#guardar sumário da execução (hp)
	best_model = tuner.get_best_models(num_models=1)[0]
	best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

	now = datetime.now()
	fim = time.time()
	t4 = fim - inicio
	log = open('RS.txt', 'a')
	log.write("------ Excecução encerrada em: " + str(now) + "\n\nTempo de execução: " + str(t4) )
	log.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/RS.txt')
	shutil.move(caminho_origem, caminho_destino)

	model = best_model

	now = datetime.now()
	log = open('TreinoMA.txt', 'a')
	log.write("------Modelo Adaptado Excecução iniciada em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()

	history = model.fit(train_X1, train_y1, epochs=5000, validation_data=(test_X1, test_y1))

	now = datetime.now()
	fim = time.time()
	t5 = fim - inicio
	log = open('TreinoMA.txt', 'a')
	log.write("------ Excecução Total encerrada em: " + str(now) + "\n\nTempo de execução: " + str(t5) )
	log.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/TreinoMA.txt')
	shutil.move(caminho_origem, caminho_destino)

	now = datetime.now()
	log = open('CalcCKT.txt', 'a')
	log.write("------Cálculos com KT iniciados em: " + str(now) + "\n\n")
	log.close()
	inicio = time.time()


	# make a prediction
	yhat1 = model.predict(test_X1)
	test_X1 = test_X1.reshape((test_X1.shape[0], test_X1.shape[2]))
	# invert scaling for forecast
	inv_yhat1 = concatenate((test_X1, yhat1), axis=1)
	inv_yhat1 = scaler.inverse_transform(inv_yhat1)
	inv_yhat1 = inv_yhat1[:,-1]
	# invert scaling for actual
	test_y1 = test_y1.reshape((len(test_y1), 1))
	inv_y1 = concatenate((test_X1, test_y1), axis=1)
	inv_y1 = scaler.inverse_transform(inv_y1)
	inv_y1 = inv_y1[:,-1]

	#print(model.summary())

	#from ann_visualizer.visualize import ann_viz

	#ann_viz(model, title="My first neural network")

	# calculate RMSE
	rmse = sqrt(mean_squared_error(inv_y1, inv_yhat1))
	desvioAmostralpred1 = np.std(inv_yhat1) #desvio padrão populacional
	varianciaAmostralpred1 = inv_yhat1.var() #variancia populacional

	desvioAmostralreal1 = np.std(inv_y1) #desvio padrão populacional
	varianciaAmostralreal1 = inv_y1.var() #variancia populacional

	slope, intercept, r_value, p_value, std_err = stats.linregress(inv_y1, inv_yhat1)


	coeffs1 = np.polyfit(inv_y1, inv_yhat1, 5)
	p1 = np.poly1d(coeffs1)
	# fit values, and mean
	yhat1 = p1(inv_y1)							  # or [p(z) for z in x]
	ybar1 = np.sum(inv_yhat1)/len(inv_yhat1)		   # or sum(y)/len(y)
	ssreg1 = np.sum((yhat1-ybar1)**2)			   # or sum([ (yihat - ybar)**2 for yihat in yhat])
	sstot1 = np.sum((inv_yhat1 - ybar1)**2)			 # or sum([ (yi - ybar)**2 for yi in y])
	r1 = ssreg1 / sstot1

	now = datetime.now()
	fim = time.time()
	t6 = fim - inicio
	log = open('CalcCKT.txt', 'a')
	log.write("------ Cálculos encerrados em: " + str(now) + "\n\nTempo de execução: " + str(t6) )
	log.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/CalcCKT.txt')
	shutil.move(caminho_origem, caminho_destino)

	erro = []
	for x in inv_yhat1:
		erro = inv_yhat1 - inv_y1

	#Boxplot
	fig1, ax1 = pyplot.subplots()
	pyplot.boxplot([inv_y1, inv_yhat1, erro], labels=['Real', 'Predito', 'Erro'])
	pyplot.title('P20 - Infestado')
	dpi = fig1.get_dpi()

	# Salva a figura no Google Drive
	pyplot.savefig('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/GBoxP_CKT.png', dpi=dpi*2)

	# Exibe o gráfico na tela

	#Gráfico de Dispersão
	pyplot.scatter(inv_yhat1, inv_y1)
	range = [inv_y1.min(), inv_yhat1.max()]
	pyplot.xlim(left=0)
	pyplot.xlim(right=8000)
	pyplot.ylim(bottom=0)
	pyplot.ylim(top=8000)
	pyplot.plot(range, range, 'red')
	pyplot.title('P20 Infestado - Real x Predito')
	pyplot.ylabel('Real')
	pyplot.xlabel('Predito')
	pyplot.savefig(f'GDisp_CKT.png', dpi=dpi*2)


	pyplot.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/GBoxP_CKT.png')
	shutil.move(caminho_origem, caminho_destino)
	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/GDisp_CKT.png')
	shutil.move(caminho_origem, caminho_destino)
	
	#print('P20 - Infestado')
	#print("R2 linear", r_value ** 2)
	#print("R2 Polinomial:", r1)
	#print('Test RMSE: %.3f' % rmse)
	#print("Desvio Real", desvioAmostralreal1)
	#print("Variancia Real", varianciaAmostralreal1)
	#print("Desvio Predito", desvioAmostralpred1)
	#print("Variancia Predito", varianciaAmostralpred1)
	#print('Real')
	#print(inv_y1)
	#print('Predito')
	#print(inv_yhat1)

	file = open('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/Log_CKT.txt', "w")
	file.write('P20 - Infestado' + '\n')
	file.write('Test RMSE:' + '%.3f' % rmse + '\n')
	file.write('R2 linear:' + str(r_value ** 2) + '\n')
	file.write("R2 Polinomial:" + str(r1) + '\r')
	file.write("Desvio Real:" + str(desvioAmostralreal1) + '\n')
	file.write("Variancia Real:" + str(varianciaAmostralreal1) + '\n')
	file.write("Desvio Predito:" + str(desvioAmostralpred1) + '\n')
	file.write("Variancia Predito:" + str(varianciaAmostralpred1) + '\n')
	file.write('Real' + '\n')
	for a in inv_y1:
		file.write(str('%.2f' % a) + ',' + ' ')
	file.write('\n' + 'Predito' + '\n')
	for b in inv_yhat1:
		file.write(str('%.2f' % b) + ',' + ' ')
	file.close()

	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/Log_CKT.txt')
	shutil.move(caminho_origem, caminho_destino)

	media1=t1+media1
	media2=t2+media2
	media3=t3+media3
	media4=t4+media4
	media5=t5+media5
	media6=t6+media6

	aux = aux+1
	
	caminho_origem = str('/home/bianca/Área de Trabalho/MODELO/MODELO ADAPTADO/GRU/KT')
	shutil.move(caminho_origem, caminho_destino)
	
	
media1=media1/valor_inteiro
media2=media2/valor_inteiro
media3=media3/valor_inteiro
media4=media4/valor_inteiro
media5=media5/valor_inteiro
media6=media6/valor_inteiro
	
log = open(f'log_medias_{str(nomelogmedia)}.txt', 'a')

log.write("A média de tempo de manipulação dos dados é: " + str(media1) + "s\n\n")
log.write("A média de tempo de execução de Definição do modelo e Treinamento sem KT é: " + str(media2) + "s\n\n")
log.write("A média de tempo dos cálculos sem KT é: " + str(media3) + "s\n\n")
log.write("A média de tempo de execução da Random Search é: " + str(media4) + "s\n\n")
log.write("A média de tempo de execução do Treinamento com KT é: " + str(media5) + "s\n\n")
log.write("A média de tempo dos cálculos com KT é: " + str(media6) + "s\n\n")

log.close()


