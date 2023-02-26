def find_eligible_students( student_names, marks_obtained, total_marks, exam_results, required_percentile):
   
    # Combine student data into a list of tuples
    student_data = list(zip(student_names, marks_obtained, exam_results))
    
    # Sort students by marks obtained in descending order
    student_data.sort(key=lambda x: x[1], reverse=True)
    
    # Compute rank and percentile score for each student
    total_students = len(student_data)
   
    for i, student in enumerate(student_data):  #iterate over a sequence
        rank = i + 1                            #rank of the current student is calculated by adding 1 to their index
        
        percentile = (total_students - rank) / total_students * 100     
        student_data[i] = (student[0], student[1], student[2], percentile)      #student[0]==student_names , student[1]==marks_obtained, student[2]==exam_results
    
    # Filter out failed students and those with percentile below required
    eligible_students = [student[0] for student in student_data if student[2] == "Passed" and student[3] >= required_percentile]
    
    # Sort eligible students by percentile score in descending order
    eligible_students.sort(key=lambda x: student_data[student_names.index(x)][3], reverse=True)  
    
    return eligible_students
# Example usage
students = ["Kartik" ,"Devang", "Pari", "Ketan", "Sheetal", "Darshana", "Mohan"]
marks_obtained = [800, 300, 750, 760, 680, 790, 640]
total_marks = 1000
exam_result = ["Passed", "Failed", "Passed", "Failed", "Passed", "Passed", "Passed"]
eligibility_percentile = 50

eligible_students = find_eligible_students(students, marks_obtained, total_marks, exam_result, eligibility_percentile)
print("Eligible students:", eligible_students)
