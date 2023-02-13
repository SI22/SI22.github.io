Question:
- id (int, primary key)
- title (text)
- content (text)
- author (text)
- date_posted (datetime)

Answer:
- id (int, primary key)
- content (text)
- author (text)
- question_id (int, foreign key to Question.id)
- date_posted (datetime)
