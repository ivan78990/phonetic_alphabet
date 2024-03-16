# import random
#
# names = ["Ivan", "Victor", "Tolya", "Dima", "Kolya", "Sergey"]
#
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split()
# word_dict = {word: len(word) for word in word_list}

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

my_dict = {"student": ["Ivan", "Victor", "Tolya"],
           "score": [55, 34, 94]
}
import pandas

df = pandas.DataFrame(my_dict)
print(df)
for (index, row) in df.iterrows():
    print(row.student, row.score)
