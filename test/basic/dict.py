nameAndScores = {'ZXC': 22, 'WYL': 18};
print(nameAndScores['ZXC']);
nameAndScores['ZXC'] = 23;
print(nameAndScores['ZXC']);
print('22' in nameAndScores);
print(nameAndScores.get('ZXC', 'WYL'));
print('------------------------');
print(nameAndScores.pop('ZXC'));
print(nameAndScores);
key = (1,);
nameAndScores[key] = "OK";
print(nameAndScores);

