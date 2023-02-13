from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knowledge_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knowledge_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    title = data['title']
    content = data['content']
    question = Question(title=title, content=content)
    db.session.add(question)
    db.session.commit()
    return jsonify({'message': 'Question added successfully!', 'id': question.id})

@app.route('/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get(id)
    answers = []
    for answer in question.answers:
        answers.append({'id': answer.id, 'content': answer.content})
    return jsonify({'title': question.title, 'content': question.content, 'answers': answers})

@app.route('/answers', methods=['POST'])
def add_answer():
    data = request.get_json()
    content = data['content']
    question_id = data['question_id']
    answer = Answer(content=content, question_id=question_id)
    db.session.add(answer)
    db.session.commit()
    return jsonify({'message': 'Answer added successfully!', 'id': answer.id})


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    title = data['title']
    content = data['content']
    question = Question(title=title, content=content)
    db.session.add(question)
    db.session.commit()
    return jsonify({'message': 'Question added successfully!', 'id': question.id})

@app.route('/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get(id)
    answers = []
    for answer in question.answers:
        answers.append({'id': answer.id, 'content': answer.content})
    return jsonify({'title': question.title, 'content': question.content, 'answers': answers})

@app.route('/answers', methods=['POST'])
def add_answer():
    data = request.get_json()
    content = data['content']
    question_id = data['question_id']
    answer = Answer(content=content, question_id=question_id)
    db.session.add(answer)
    db.session.commit()
    return jsonify({'message': 'Answer added successfully!', 'id': answer.id})
