def student_screener(students, percentile_criteria):
    #percentile score for each student
    for student in students:
        percentile_score = (student['marks_obtained'] / student['total_marks']) * 100

        # Add the percentile score to the student's data
        student['percentile_score'] = percentile_score

    # Sort students by their percentile score in descending order
    sorted_students = sorted(students, key=lambda x: x['percentile_score'], reverse=True)

    # cutoff percentile score based on the percentile criteria
    cutoff_percentile_score = sorted_students[int(len(sorted_students) * percentile_criteria / 100)]['percentile_score']

    # Filter the eligible students based on the cutoff percentile score
    eligible_students = [student for student in sorted_students if student['percentile_score'] >= cutoff_percentile_score and student['result'] == 'Passed']

    return eligible_students

  #Sample data
students = [
    {'name': 'Kartik', 'marks_obtained': 800, 'total_marks': 1000, 'result': 'Passed'},
    {'name': 'Devang', 'marks_obtained': 300, 'total_marks': 1000, 'result': 'Failed'},
    {'name': 'Pari', 'marks_obtained': 750, 'total_marks': 1000, 'result': 'Passed'},
    {'name': 'Ketan', 'marks_obtained': 760, 'total_marks': 1000, 'result': 'Failed'},
    {'name': 'Sheetal', 'marks_obtained': 680, 'total_marks': 1000, 'result': 'Passed'},
     {'name': 'Darshana', 'marks_obtained': 790, 'total_marks': 1000, 'result': 'Passed'},
    {'name': 'Mohan', 'marks_obtained': 640, 'total_marks': 1000, 'result': 'Passed'}
]

percentile_criteria = 50

# Find eligible students
eligible_students = student_screener(students, percentile_criteria)

# Print the eligible students
for student in eligible_students:
    print(student['name'])
