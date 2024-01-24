from sklearn import tree

#[height, weight, shoe size]
X = [
    [181, 80, 44], [157, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [167, 70, 40],
    [159, 55, 37], [171, 75, 42], [181, 85, 43]
]


Y = [
    ' male ', ' female ', ' female ', ' female ',
    ' male ',' male ', ' male ', ' female ',
    ' male ', ' female ', ' male '
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

def fxy(alt,pes,zap):
  prediction = clf.predict([[alt,pes,zap]])
  X.append([alt,pes,zap])
  Y.append(prediction[0])
  return prediction[0]

control = True
while control:
  alt = int(input("Insert the person's height in CM: "))
  pes = int(input("Insert the person's weight in KG: "))
  zap = int(input("Insert shoe size: "))
  prd= fxy(alt,pes,zap)
  print(prd)
  repeat = input("Do you want to make another query? (yes/no): ")
  if repeat.lower() == "no":
     control = False
  elif repeat.lower() == "yes":
    control = True

print(X)
print(Y)
