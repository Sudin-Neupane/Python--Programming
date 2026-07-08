import matplotlib.pyplot as plt

students = ["Sudin", "Ashwin", "Ajit", "Asak", "Dipsan", "Sudarshan"]
scores = [82, 91, 76, 89, 68, 94]

plt.figure(figsize=(10, 6))
plt.bar(students, scores, color=["#4C72B0", "#55A868", "#C44E52", "#8172B3", "#CCB974", "#64B5CD"])
plt.ylim(0, 100)
plt.title("Student Result Bar Graph")
plt.xlabel("Student")
plt.ylabel("Score")
plt.grid(axis="y", linestyle="--", alpha=0.5)

for index, score in enumerate(scores):
    plt.text(index, score + 2, str(score), ha="center", va="bottom")

plt.show()