prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta=[14, 23, 15, 14, 12, 41, 39]
for i in range(0,len(prenume)):
    print(prenume[i],'are varsta de',varsta[i],'ani')
    i+=1
prenume.extend(['Andreea', 'Ioan'])
varsta.extend([34,23])
print(prenume,'\n',varsta)
prenume.pop(2)
varsta.pop(2)
print(prenume,'\n',varsta)
print(prenume[0:3])
print(prenume[::-1])
print(prenume[2],prenume[4],varsta[2],varsta[4])
print(prenume[0:6])
print(varsta[0:6])