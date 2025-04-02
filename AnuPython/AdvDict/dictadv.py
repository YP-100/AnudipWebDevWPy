#demo 1 ****************************

scores = [
    {"student":"alice","subject":"math","score":90},
    {"student":"alice","subject":"english","score":85},
    {"student":"bob","subject":"math","score":75},
    {"student":"bob","subject":"english","score":80},
    {"student":"charlie","subject":"math","score":88}
]

student_scores = {
    student : max(items['score'] for items in scores if items['student'] == student)
    for student in (item['student']for item in scores)
}
print(student_scores)

#demo 2 ********************************

items = [
    {"name":"Apple","category":"fruit"},
    {"name":"Banana","category":"fruit"},
    {"name":"carrot","category":"vagetable"},
    {"name":"brocoli","category":"vegetable"},
    {"name":"chicken","category":"meat"},
]

category_items = {
    category : [item['name'] for item in items if item['category']==category]
    for category in {item['category']for item in items}
}
for i,j in category_items.items():
    print(i,j)