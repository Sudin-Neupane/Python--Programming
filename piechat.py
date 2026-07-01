import matplotlib.pyplot as plt

students = ["Sudin", "Ashwin", "Ajit", "Asak", "Dipsan", "Sudarshan"]
scores = [82, 91, 76, 89, 68, 94]

plt.figure(figsize=(10, 6))
plt.pie(scores, labels=students, colors=["#4C72B0", "#55A868", "#C44E52", "#8172B3", "#CCB974", "#64B5CD"], autopct="%1.1f%%")
plt.title("Student Result Pie Chart")

for index, score in enumerate(scores):
    plt.text(index, score + 2, str(score), ha="center", va="bottom")

plt.show()