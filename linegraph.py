import matplotlib.pyplot as plt

students = ["Sudin", "Ashwin", "Ajit", "Asak", "Dipsan", "Sudarshan"]
scores = [82, 91, 76, 89, 68, 94]

plt.figure(figsize=(10, 6))
plt.plot(students, scores, marker="o", linestyle="-", color="#4C72B0", linewidth=2)
plt.title("Student Result Line Graph")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for index, score in enumerate(scores):
    plt.text(index, score + 1.5, str(score), ha="center", va="bottom")

plt.show()