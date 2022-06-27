from datetime import datetime

data = datetime.now()
print('O tipo de dado inicial é: ', type(data))
data_em_texto = data.strftime('%d/%m/%Y %H:%M')
data = data_em_texto
print('O tipo de dado final é: ',type(data))
print('O conteúdo do dado é: ',data)
print('------------------------------')


date = datetime.strptime(data, '%d/%m/%Y %H:%M')

<<<<<<< HEAD
print(date, type(date))
=======
print(date, type(date))
>>>>>>> 54f780f37029f36fa764a52d33eadc97d8469e6d
