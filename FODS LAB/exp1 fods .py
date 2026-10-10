import numpy as np

# Rows represent students; columns: Math, Science, English, History
student_scores = np.array([
    [85, 78, 92, 80],
    [90, 88, 85, 75],
    [76, 95, 89, 84],
    [88, 82, 91, 90]
])

# Calculate the average score for each subject (column-wise)
subject_averages = np.mean(student_scores, axis=0)
subjects = ["Math", "Science", "English", "History"]

print("Average score for each subject:")
for subject, average in zip(subjects, subject_averages):
    print(f"{subject}: {average:.2f}")

# Find the subject with the highest average
highest_index = np.argmax(subject_averages)
print(f"Subject with the highest average: {subjects[highest_index]} "
      f"({subject_averages[highest_index]:.2f})")
