def find_eligible_students(students, marks_obtained, total_marks, exam_result, eligibility_percentile):

    # Calculate the percentile rank of each student
    percentile_ranks = [100*(sum([1 for j in marks_obtained if j<=marks_obtained[i]])-1)/(len(marks_obtained)-1) for i in range(len(students))]
    
    # Find the cutoff percentile based on the eligibility percentile
    cutoff_percentile = max(percentile_ranks) - (max(percentile_ranks) - min(percentile_ranks)) * eligibility_percentile/100
    
    # Create a list of eligible students
    eligible_students = [students[i] for i in range(len(students)) if percentile_ranks[i] >= cutoff_percentile and exam_result[i]=="Passed"]
    
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
