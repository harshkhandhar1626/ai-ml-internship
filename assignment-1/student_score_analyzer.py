# Assignment 1 - Student Score Analyzer
# Name: Harsh Khandhar
# AI Internship - MINDS INVASION

# ---------------------- Python Basics ----------------------

# Store the marks of 10 students in a Python list.
# These marks will be used for grading and statistical analysis.
marks = [72, 85, 90, 45, 63, 78, 91, 56, 88, 67]

# This function assigns grades based on the student's score.
# A = 85 or above
# B = 70 to 84
# C = 50 to 69
# F = Below 50
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

# Print each student's score along with the assigned grade.
print("Student Scores and Grades")
for i, score in enumerate(marks, start=1):
    print(f"Student {i}: {score} -> {grade(score)}")

# ---------------------- NumPy Analysis ----------------------

# Import the NumPy library.
# NumPy is used for fast numerical and statistical calculations.
import numpy as np

# Convert the Python list into a NumPy array.
scores = np.array(marks)

# Calculate and display statistical values.
print("\n----- Statistics -----")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Maximum Score:", np.max(scores))
print("Minimum Score:", np.min(scores))
print("Standard Deviation:", np.std(scores))

# Calculate the class average.
average = np.mean(scores)

# Find students who scored above the class average using Boolean masking.
above_average = scores[scores > average]

print("\nClass Average:", average)
print("Number of Students Above Average:", len(above_average))

# Print only A-grade students (85 or above) without using a loop.
a_grade = scores[scores >= 85]

print("A Grade Scores:", a_grade)

# ---------------------- Bonus Task ----------------------

# Add five more student scores.
extra_marks = [80, 94, 61, 48, 75]

# Combine the original and new scores into one array.
all_scores = np.append(scores, extra_marks)

print("\n----- Bonus Analysis -----")
print("Updated Mean:", np.mean(all_scores))
print("Updated Median:", np.median(all_scores))
print("Updated Maximum:", np.max(all_scores))
print("Updated Minimum:", np.min(all_scores))
print("Updated Standard Deviation:", np.std(all_scores))

# Generate grades for all students.
grades = [grade(score) for score in all_scores]

# Count the number of students in each grade category.
grade_count = {}

for g in grades:
    if g in grade_count:
        grade_count[g] += 1
    else:
        grade_count[g] = 1

print("\nGrade Count:")
for key, value in grade_count.items():
    print(key, ":", value)

# Find the grade category with the highest number of students.
most_common = max(grade_count, key=grade_count.get)

print("\nMost Common Grade:", most_common)

# ---------------------- End of Program ----------------------
# This program stores student marks, assigns grades,
# performs statistical analysis using NumPy,
# and identifies the most common grade category.
