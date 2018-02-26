from sklearn import tree
features = [[14,1],[12,0],[16,1],[17,0]]
labels = [0,0,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([14,1])
