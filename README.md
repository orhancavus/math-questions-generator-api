# Math Questions Generator API

This is a simple Flask application that generates 20 random math questions for addition, subtraction, multiplication, and division, and allows users to validate their answers.

```text
Author : Orhan Cavus
Date   : 01.04.2023
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/orhancavus/math-questions-generator-api.git
    ```

2. Change into the project directory:

    ```bash
    cd math-questions-generator-api
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    python app.py
    ```

## API Endpoints

### GET /get_math_questions

Generates 20 random math questions for addition, subtraction, multiplication, and division.

Example response:

```bash
[
    {
        "id": 1,
        "question": "7 * 51 = ?",
        "answer": 357
    },
    {
        "id": 2,
        "question": "75 / 25 = ?",
        "answer": 3
    },
    ...
]
```

### POST /validate_answers

Validates the user's answers to the math questions.

Example request:

```bash
{
    "questions": [
        "7 * 51 = ?",
        "75 / 25 = ?",
        ...
    ],
    "answers": [
        357,
        3,
        ...
    ]
}
```

Example response:

```bash
[
    {
        "id": 1,
        "question": "7 * 51 = ?",
        "correct_answer": 357,
        "user_answer": 357,
        "is_correct": true
    },
    {
        "id": 2,
        "question": "75 / 25 = ?",
        "correct_answer": 3,
        "user_answer": 5,
        "is_correct": false
    },
    ...
]
```

## API Usage
The API has two endpoints:

* `/get_math_questions` - Returns 20 random math questions in JSON format.
* `/validate_answers` - Accepts a JSON payload of questions and answers, and returns a JSON response indicating whether each answer is correct or incorrect.

### Example Requests

`/get_math_questions`

```bash
GET http://localhost:5000/get_math_questions
```

`/validate_answers`

```bash
POST http://localhost:5000/validate_answers
Content-Type: application/json

{
    "questions": [
        "7 + 8 = ?",
        "32 / 4 = ?",
        "15 - 4 = ?"
    ],
    "answers": [
        15,
        8,
        11
    ]
}
```

### Example Responses

`/get_math_questions`

```bash
[    {        "id": 1,        "question": "22 * 63 = ?",        "answer": 1386    },    {        "id": 2,        "question": "75 - 94 = ?",        "answer": -19    },    ...]
```

`/validate_answers`

```bash
[
    {
        "id": 1,
        "question": "7 + 8 = ?",
        "correct_answer": 15,
        "user_answer": 15,
        "is_correct": true
    },
    {
        "id": 2,
        "question": "32 / 4 = ?",
        "correct_answer": 8,
        "user_answer": 9,
        "is_correct": false
    },
    {
        "id": 3,
        "question": "15 - 4 = ?",
        "correct_answer": 11,
        "user_answer": 12,
        "is_correct": false
    }
]
```

### Docker image

```bash
docker build -t math_questions_app .
docker run -p 5000:5000 math-questions-generator-api
```


### Run the tests using pytest in your terminal:

$ pytest
