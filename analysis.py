import numpy as np
students =100
subjects=3
marks = np.random.randint(35,101, size=(students, subjects))
print("shape of marks array:", marks.shape)
# print(marks)
subjects_name = ["Physics", "Math", "Chemistry"]
# print(marks[0]) -> first student details
# print(marks[:,0]) ->  all physics marks 
# print(marks[:,1]) ->  all math marks 
# print(marks[:,2]) ->  all chemistry marks 

print("First 5 students:\n", marks[:5])

# Basic Statistics (Core NumPy)

mean_scores = np.mean(marks, axis=0)
print("Mean Scores:", mean_scores)

median_scores = np.median(marks, axis=0)
print("Median Scores:", median_scores)

std_scores = np.std(marks, axis=0)
print("Standard Deviation:", std_scores)

subjects_names = ["Math", "Physics", "CS"]

print("\n===== Average Scores =====")
for i in range(len(subjects_names)):
    print(f"{subjects_names[i]}: {mean_scores[i]:.2f}")

total_scores = np.sum(marks, axis=1)
print("First 5 total scores:", total_scores[:5])

top_student_index = np.argmax(total_scores)
top_student_score = total_scores[top_student_index]

top_5_indices = np.argsort(total_scores)[-5:][::-1]

print("\n===== Top Student =====")
print(f"Student ID: {top_student_index}")
print(f"Total Score: {top_student_score}")

print("\n===== Top 5 Students =====")
for idx in top_5_indices:
    print(f"Student {idx} - Total: {total_scores[idx]}")
