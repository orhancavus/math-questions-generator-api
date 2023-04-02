from app import app
import json
import pytest

def test_home_endpoint():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome to Math Questions Generator API!' in response.data

def test_get_math_questions_endpoint():
    with app.test_client() as client:
        response = client.get('/get_math_questions')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 20
        for question in data:
            assert 'id' in question
            assert 'question' in question
            assert 'answer' in question

def test_validate_answers_endpoint():
    data = {
        "questions": ["5 + 3 = ?", "10 - 4 = ?"],
        "answers": [8, 6]
    }
    with app.test_client() as client:
        response = client.post('/validate_answers', json=data)
        assert response.status_code == 200
        result = response.get_json()
        assert len(result) == 2
        for res in result:
            assert 'id' in res
            assert 'question' in res
            assert 'correct_answer' in res
            assert 'user_answer' in res
            assert 'is_correct' in res
