import mysql.connector

# dbect to the existing 'quizapp' database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mypass", #this is an dummy password you need to use yours
    database="quizapp"
)

cursor = db.cursor()

name = input("Please enter your name: ")
cursor.execute("SELECT password, score, highscore FROM scores WHERE name = %s", (name,))
result = cursor.fetchone()

#Check if the user esixt ig yes check password and print previous scores 
if result:
    saved_password, previous_score, highscore = result
    password_attempt = input("Please enter your password: ")
    if password_attempt != saved_password:
        print("Wrong password! Access denied.")
        db.close()
        exit()
    print(f"\nWelcome back, {name}!")
    print(f"Your previous score: {previous_score}")
    print(f"Your current high score: {highscore}")
# if no create new password and new scores
else:
    print(f"Welcome, {name}! You're a new user.")
    password = input("Please create a password for your account: ")
    cursor.execute("INSERT INTO scores (name, password, score, highscore) VALUES (%s, %s, %s, %s)", 
                   (name, password, 0, 0))
    db.commit()
    print("Account created successfully!")

# Start Quiz
score = 0
print("\nMini Quiz (from Database)")
print("\nNote: Spell correctly and add space between names if required!")
print("\n -------------------------------------------------------------- \n")

cursor.execute("SELECT question, answer FROM qna")
quiz_data = cursor.fetchall()
cursor.execute("SELECT question, answer FROM qna ORDER BY RAND() LIMIT 10")
quiz_data = cursor.fetchall()

i = 1
questioncount = 0
for qa in quiz_data:
    question = qa[0]
    correct_answer = qa[1]
    user_answer = input(f"{i}. {question} ").strip().lower()
    questioncount += 1
    if user_answer == correct_answer.strip().lower():
        score += 1
    i += 1


print(f"\nYour score: {score}/{questioncount}")

# update the scores
cursor.execute("SELECT highscore FROM scores WHERE name = %s", (name,))
current_highscore = cursor.fetchone()[0]

if score > current_highscore:
    cursor.execute("UPDATE scores SET score = %s, highscore = %s WHERE name = %s", 
                   (score, score, name))
    print("Congrats! New high score! Updated in database.")
else:
    cursor.execute("UPDATE scores SET score = %s WHERE name = %s", (score, name))
    print("Score updated, but did not beat the high score.")

db.commit()
print(f"Your current score: {score}")
print(f"Your high score: {max(score, current_highscore)}")
db.close()
