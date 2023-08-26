# Import the required modules
from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Define student and course dictionaries
students = {
    "S101": {"name": "Alice", "age": 20, "gender": "Female", "city": "New York", "courses": ["C101", "C102"]},
    "S102": {"name": "Bob", "age": 22, "gender": "Male", "city": "Los Angeles", "courses": ["C102", "C103"]},
    "S103": {"name": "Charlie", "age": 21, "gender": "Male", "city": "Chicago", "courses": ["C101"]},
    "S104": {"name": "David", "age": 23, "gender": "Male", "city": "Houston", "courses": ["C103"]},
    "S105": {"name": "Eve", "age": 20, "gender": "Female", "city": "Miami", "courses": ["C101", "C103"]},
    "S106": {"name": "Frank", "age": 24, "gender": "Male", "city": "Seattle", "courses": ["C102"]},
    "S107": {"name": "Grace", "age": 22, "gender": "Female", "city": "San Francisco", "courses": ["C101", "C102"]},
    "S108": {"name": "Harry", "age": 23, "gender": "Male", "city": "Dallas", "courses": ["C102", "C103"]},
    "S109": {"name": "Ivy", "age": 21, "gender": "Female", "city": "Boston", "courses": ["C103"]},
    "S110": {"name": "Jack", "age": 20, "gender": "Male", "city": "Atlanta", "courses": ["C101", "C102"]},
}

courses = {
    "C101": {"name": "Math", "price": 100, "instructor": "Dr. Smith", "level": "Intermediate"},
    "C102": {"name": "Science", "price": 150, "instructor": "Prof. Johnson", "level": "Advanced"},
    "C103": {"name": "History", "price": 120, "instructor": "Dr. Davis", "level": "Beginner"},
    "C104": {"name": "English", "price": 130, "instructor": "Prof. Miller", "level": "Intermediate"},
    "C105": {"name": "Physics", "price": 160, "instructor": "Dr. Wilson", "level": "Advanced"},
    "C106": {"name": "Geography", "price": 110, "instructor": "Dr. White", "level": "Beginner"},
    "C107": {"name": "Chemistry", "price": 140, "instructor": "Prof. Lee", "level": "Intermediate"},
    "C108": {"name": "Biology", "price": 170, "instructor": "Prof. Brown", "level": "Advanced"},
    "C109": {"name": "Computer Science", "price": 180, "instructor": "Dr. Martinez", "level": "Intermediate"},
    "C110": {"name": "Literature", "price": 150, "instructor": "Dr. Taylor", "level": "Advanced"},
    "C111": {"name": "Economics", "price": 130, "instructor": "Prof. Adams", "level": "Beginner"},
    "C112": {"name": "Psychology", "price": 140, "instructor": "Dr. Scott", "level": "Intermediate"},
    "C113": {"name": "Sociology", "price": 120, "instructor": "Prof. Lewis", "level": "Beginner"},
    "C114": {"name": "Philosophy", "price": 160, "instructor": "Dr. Turner", "level": "Advanced"},
    "C115": {"name": "Political Science", "price": 170, "instructor": "Prof. Hall", "level": "Intermediate"},
}


# Calculate course count for each student
for student_id, student_info in students.items():
    student_info["course_count"] = len(student_info["courses"])

# Define route to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_code = request.form['student_code']
        entered_student_code = student_code
        student_info = students.get(student_code)
        if student_info:
            student_courses = student_info['courses']
            student_course_info = [
                {
                    "course_name": courses[course]['name'],
                    "course_price": courses[course]['price']
                }
                for course in student_courses
            ]
            course_count = student_info['course_count']
            total_cost = sum(course['course_price'] for course in student_course_info)  # Calculate total cost
            return render_template('index.html', student_info=student_info, student_course_info=student_course_info, course_count=course_count, entered_student_code=entered_student_code, total_cost=total_cost)
        else:
            return "Student not found."
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
