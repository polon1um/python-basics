import sys

my_list = [12, '15', 95.32, 55, True]
print(my_list, type(my_list), id(my_list), sys.getsizeof(my_list))

student_marks = []
while True:
    mark = input('введите оценку студента:' )
    if mark: # '' == false, 0=[ false, [] == false
        student_marks.append(mark)
    else:
        break
print('ввод завершен')
print(student_marks)