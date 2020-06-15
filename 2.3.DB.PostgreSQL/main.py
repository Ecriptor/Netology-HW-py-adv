import psycopg2 as pg


def create_db(): # создает таблицы
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()

        cur.execute('DROP TABLE student_course;')
        cur.execute('DROP TABLE student;')
        cur.execute('DROP TABLE course;')

        cur.execute('''
                create table if NOT EXISTS student (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL,
                gpa NUMERIC(10, 2),
                birth TIMESTAMP WITH TIME ZONE 
            )
            ''')

        cur.execute('''
                create table if NOT EXISTS course (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL
            )
             ''')

        cur.execute('''
            create table if NOT EXISTS student_course (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES student(id),
            course_id INTEGER REFERENCES course(id)
            )
            ''')


def add_student(student): #Просто добавляем студента
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()
        cur.execute('''
        insert into student(name, gpa, birth) VALUES (%s, %s, %s)
        ''', (student['name'], student['gpa'], student['birth']))


def add_students(course_id, students): # Добавляем студентов и записываем их на курс
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()
        for student in students:
            cur.execute('''
            insert into student(name, gpa, birth) VALUES (%s, %s, %s)
            ''', (student['name'], student['gpa'], student['birth']))
            cur.execute("""
            insert into student_course (student_id, course_id) values ((select max(id) from student), %s)
            """, (course_id,))


def get_student(student_id): # Показываем студента по его ID
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()
        cur.execute('''
        SELECT * FROM student WHERE id = %s
        ''', (student_id,))
        student = cur.fetchall()
        return student


def get_students(course_id): # Возврат студентов записаных на курс
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()
        cur.execute('''
        SELECT * FROM student_course LEFT JOIN student on student_course.student_id = student.id 
        WHERE course_id = %s;''', (course_id,))
        students = cur.fetchall()
        return students


def insert_course(name): # Добавляем курс
    with pg.connect(database='netology', user='netology', password='netology', host='10.85.132.233', port=5432) as conn:
        cur = conn.cursor()
        cur.execute("""
              insert into course (name) values (%s)
              """, (name,))


if __name__ == '__main__':

    students = [{'name': 'Mark', 'gpa': 4.2, 'birth': '1984-05-14'},
                {'name': 'Elon', 'gpa': 4.8, 'birth': '1971-06-28'}]

    student = {'name': 'Bill', 'gpa': 4.5, 'birth': '1955-10-28'}

    #create_db() # создает таблицы
    #insert_course('Програмирование на PYTHON')
    #insert_course('Програмирование на JAVA')
    #insert_course('Програмирование на C++')
    #insert_course('Програмирование на Go')
    #add_students(4, students)
    #add_student(student)
    #print(get_student(2))
    #print(get_students(4))



