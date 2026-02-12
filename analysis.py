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

