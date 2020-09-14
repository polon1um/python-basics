
import sys
# to contain -> container -> arrays
# to read -> reader
# [12, 15, 95, 55, 36]
# !!! all is object !!! OOP
# объекты (пользователь)
#     - атрибуты: свойства (id, name, login, password)
#     - методы: действия (edit, delete, create, input_data)
# snake_case
# My_var
# my_Var
# myVar -> cameCase (Java, JS)
# 'ya.ru' -> reference
# my_var = [12, '15', 95.32, 55, True]  # var -> reference
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = 12
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = 12.5
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))
#
# my_var = '12.5'
# print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

student_marks = []
while True:
    mark = input('Введите оценку студента: \n')
    if mark:
        student_marks.append(mark)
    else:
        break

print('Ввод завершен')
print(student_marks)

mock_student_marks = ['5', '4', '3', '5', '2']
# mock_student_marks = [5, 4, 3, 5, 2]
# data read
# student_marks = []
# while True:
#     mark = input('Введите оценку студента: \n')
#     if mark:
#         student_marks.append (int(mark))
#     else:
#         break
#
# print('Ввод завершен')
# print(student_marks)

# mock_student_marks = ['5', '4', '3', '5', '2']
mock_student_marks = [5, 4, 3, 5, 2]
student_marks = mock_student_marks

# data processing
i = 0
avg_mark = 0
while i < len(student_marks):
#    print(type(avg_mark), type(student_marks[i]))
#    avg_mark = avg_mark + int(student_marks [i])
    avg_mark += int(student_marks[i])
#    i = i + 1
    i += 1
print(avg_mark)
# avg_mark = avg_mark / len(student_marks)
avg_mark /= len(student_marks)
print('Средний балл: ', avg_mark)
# <num1> + <num2> - binary operation
# -<num> - unary operation