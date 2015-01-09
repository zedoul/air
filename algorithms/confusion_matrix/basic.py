y_true = [0,1,1,0,0]
y_pred = [0,0,0,0,1]

y_true = [1,1]
y_pred = [1,1]

from sklearn.metrics import confusion_matrix
m = confusion_matrix(list(y_true), list(y_pred))
print m
print m[0][0]
print m[1][0]
