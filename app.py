from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    """Returns a welcome message for the API"""
    url = "http://127.0.0.1:5000/get_math_questions"
    result  = f'Welcome to Math Questions Generator API! <p><a href="{url}">{url}</p>'
    return result

@app.route('/get_math_questions', methods=['GET'])
def get_math_questions():
    """Generates 20 random math questions and returns them as JSON"""
    operator_mapping = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }
    questions = []
    for i in range(20):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator_choice = random.randint(1, 4)
        operator = operator_mapping[operator_choice]
        if operator_choice == 4:
            num1 = num1 * num2
        question = f"{num1} {operator} {num2} = ?"
        answer = eval(f"{num1} {operator} {num2}")  # evaluates the correct answer based on the operator
        question_dict = {
            "id": i+1,
            "question": question,
            "answer": answer
        }
        questions.append(question_dict)
    return jsonify(questions)

@app.route('/validate_answers', methods=['POST'])
def validate_answers():
    """Validates a list of answers for a list of questions and returns the results as JSON"""
    data = request.get_json()
    questions = data["questions"]
    answers = data["answers"]
    result = []
    for i in range(len(questions)):
        question = questions[i]
        answer = answers[i]
        correct_answer = eval(question.split("=")[0])  # evaluates the correct answer based on the question
        result_dict = {
            "id": i+1,
            "question": question,
            "correct_answer": correct_answer,
            "user_answer": answer,
            "is_correct": correct_answer == answer
        }
        result.append(result_dict)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
