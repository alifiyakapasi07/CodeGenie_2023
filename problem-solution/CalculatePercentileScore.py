def percentile_score(marks_list, yourmark):

    # Get number of students who scored less than ypur marks 
    less_than_yourmark = len([mark for mark in marks_list if mark < yourmark])

    # Calculate the percentile score
    total_students = len(marks_list)
    percentile = (less_than_yourmark / total_students) * 100

    return percentile

marks = [800, 300, 950, 760, 680, 490, 640]
yourmark = 760
percentile = percentile_score(marks, yourmark)
print(f'Percentile score for {yourmark} marks is {percentile: ,.2f}')
