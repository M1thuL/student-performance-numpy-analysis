# 📊 Student Performance Analytics using NumPy

## 🚀 Project Overview

This project analyzes student performance using **NumPy**.
It demonstrates how NumPy can be used for data generation, statistical analysis, and ranking without using pandas or machine learning libraries.

The goal of this project is to strengthen core Python and NumPy concepts while building a clean, GitHub-ready data analysis project.

---

## 🧠 Concepts Used

* NumPy arrays (2D data representation)
* Random data generation
* Mean, Median, Standard Deviation
* Array slicing & indexing
* Row-wise and column-wise operations (`axis`)
* Ranking using `argsort()` and `argmax()`

---

## 📂 Dataset (Generated)

The dataset is simulated using NumPy:

* 100 students
* 3 subjects:

  * Math
  * Physics
  * Computer Science
* Marks range: **35 – 100**

Each row represents a student, and each column represents a subject.

Example structure:

```
[[78 65 89]
 [92 71 55]
 [60 40 73]]
```

---

## 📊 Features Implemented

### ✔ Data Generation

* Random marks generation using `np.random.randint()`

### ✔ Statistical Analysis

* Mean per subject
* Median per subject
* Standard deviation per subject

### ✔ Student Ranking

* Total score calculation
* Top student detection
* Top 5 students ranking

---

## ▶️ How to Run

1. Clone the repository
2. Open the project folder
3. Run:

```bash
python analysis.py
```

---

## 📌 Example Output

```
===== Average Scores =====
Math: 72.45
Physics: 69.82
CS: 75.31

===== Top Student =====
Student ID: 23
Total Score: 289
```

---

## 🎯 What I Learned

* Working with multidimensional NumPy arrays
* Using axis operations correctly
* Performing statistical analysis with NumPy
* Ranking and sorting data efficiently
* Structuring a beginner data analysis project

---

## 🔥 Future Improvements

* Add visualization using Matplotlib
* Add failure analysis
* Add correlation analysis
* Convert to Pandas-based project

---

## 👨‍💻 Author

Mithul Narayana
