import matplotlib.pyplot as plt
numofgames =[3, 5, 2, 6, 7, 1, 2, 7, 1, 7]
scores =[80, 90, 75, 80, 90, 50, 65, 85, 40, 100]
teams=['A','B','C','D','E','E','F','G','H','I']
plt.scatter(numofgames, scores, c ="blue", marker='o', linewidths=0.25)
plt.title("Game Scores")
plt.xlabel("#Games")
plt.ylabel("Scores")
#Labeling Scatter plot
for i,txt in enumerate(teams):
 plt.annotate(txt, (numofgames[i], scores[i]))
# To show the plot
plt.show()