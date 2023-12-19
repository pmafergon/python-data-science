from sklearn import tree

#[height, weight, shoe size]
X = [
    [181, 80, 44], [157, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [167, 70, 40],
    [159, 55, 37], [171, 75, 42], [181, 85, 43]
]

Y = ['male','female','female','female',
     'male','male','male','female',
     'male','female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

def fxy():
    alt = int(input("Inserte la altura de la persona en CM: "))
    pes = int(input("Inserte el peso de la persona en KG: "))
    zap = int(input("Inserte talla de zapatos: "))
    prediction = clf.predict([[alt,pes,zap]])
    print(prediction)
    X.append([alt,pes,zap])
    Y.append(prediction[0])
    
control = True
while control:
    fxy()
    repeat = input("¿Quieres realizar otra consulta? (si/no): ")
    if repeat.lower() == "no":
        control = False
    elif repeat.lower() == "si":
        control = True

print(X)
print(Y)
