# 1. sorting and ordering data
students = [
    {'name':'Durga','grade':'99'},
    {'name':'anshu','grade': '68'},
    {'nmae':'ABC','grade': '55'}
]
# sorting stds. by grade
sorted_stds = sorted(students, key=lambda x: x['grade'])
print(sorted_stds)