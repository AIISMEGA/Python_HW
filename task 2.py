checklist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final_list = [ checklist[num] for num in range(1,len(checklist)) if checklist[num] > checklist[num -1]]
print(final_list)
