student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        student_marks.append(int(mark))
        if int(mark) > 5:
            print('такой оценки не существует!')
            student_marks.remove(int(mark))
        elif int(mark) == 0:
            print('такой оценки не существует!')
            student_marks.remove(int(mark))
    else:
        break
print('Ввод завершен')
avg_mark = 0
for marks in student_marks:
    avg_mark += marks
avg_mark /= len(student_marks)
if not student_marks:
    print('Пусто)')
else:
    print('Оценки:', student_marks)
    print('Средний балл:', avg_mark)

lesson_dates = [
    '09.09.20',
    '11.09.20',
    '12.09.20',
    '22.10.20',
    '12.11.20',
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    4,
    3,
    5,
    5,
    4
]
date = input('Введите дату:\n')
for lesson_dates, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):
    print(lesson_dates, 'оценка', mark, mark_2)
