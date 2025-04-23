
import mysql.connector

# connect to the existing 'quizapp' database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ysql@1092",
    database="quizapp"
)

cursor = db.cursor()

# clear user data or questions
# cursor.execute("TRUNCATE TABLE scores")
# cursor.execute("TRUNCATE TABLE qna")
# conn.commit()
# print("Tables truncated successfully!")


# create table 'scores' if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    name VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    score INT NOT NULL,
    highscore INT NOT NULL
)
""")

#Create table 'qna' if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS qna (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL UNIQUE,
    answer VARCHAR(100) NOT NULL
)
""")

# insert questions and answers in table note - comment existing questions:

questions_data = [
        ("What is the capital of India?", "delhi"),
        ("What is 2 + 2?", "4"),
        ("What is 15 * 2?", "30"),
        ("Who is the father of computer?", "charles babbage"),
        ("Who invented bulb?", "thomas edison"),
        ("What is value of pi? _._ _", "3.14"),
        ("What is needed to run javascript outside the browser? ____js", "node"),
        ("What is square root of 9?", "3"),
        ("What is national sport of India?", "hockey"),
        ("How many colors are there in rainbow?", "7")
        ("What is the national language of india?", "hindi"),
        ("who is the national animal of india","tiger")
    ]
cursor.executemany("INSERT INTO qna (question, answer) VALUES (%s, %s)", questions_data)
db.commit()
