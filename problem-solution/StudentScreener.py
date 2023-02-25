def find_eligible_students(students, marks_obtained, total_marks, exam_results, percentile):
    
    # Calculate the scores of each student as a percentage
    scores = [marks / total_marks * 100 for marks in marks_obtained]
    
    # Combine the student data into a list of tuples
    student_data = list(zip(students, scores, exam_results))
    
    # Sort the student data by their scores in descending order
    student_data.sort(key=lambda x: x[1], reverse=True)         # lamba x:x[1]==use the second element of each tuple as the key for sorting
    
    # Calculate the cutoff score based on the percentile criteria
    cutoff_index = int(len(student_data) * (percentile / 100.0))
    cutoff_score = student_data[cutoff_index - 1][1]
    
    # Filter the eligible students based on their scores and exam results
    
    #for each student tuple in the sublist of student_data up to the cutoff_index, if the student's score is greater than or equal to the score of the 
    #student at the cutoff index and the student passed the exam, include their name in a new list of eligible students
    eligible_students = [student[0] for student in student_data[:cutoff_index] if student[1] >= cutoff_score and student[2] == "Passed"]
    
    # Return the list of eligible students
    return eligible_students

# Example usage
students = ["Kartik" ,"Devang", "Pari", "Ketan", "Sheetal", "Darshana", "Mohan"]
marks_obtained = [800, 300, 750, 760, 680, 790, 640]
total_marks = 1000
exam_result = ["Passed", "Failed", "Passed", "Failed", "Passed", "Passed", "Passed"]
eligibility_percentile = 50

eligible_students = find_eligible_students(students, marks_obtained, total_marks, exam_result, eligibility_percentile)
print("Eligible students:", eligible_students)
