student = eval((input("Enter the students: ")))
cookie = eval((input("Enter the cookies: ")))
student.sort()
cookie.sort()
studentIndex = 0
cookieIndex = 0
# Try to assign cookies until any one list is fully processed
while studentIndex < len(student) and cookieIndex < len(cookie):
            # If the cookie satisfies the student's greed
    if cookie[cookieIndex] >= student[studentIndex]:
        studentIndex += 1
            # Move to next cookie in both cases
    cookieIndex += 1

        # Number of students satisfied is equal to studentIndex
print(studentIndex)