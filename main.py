from datetime import datetime, date

def calculate_age():
    while True:
        try:
            userBirthday = input("Enter your birthdate (YYYY-MM-DD): ")
            formatDate = datetime.strptime(userBirthday, "%Y-%m-%d").date()
            today = date.today()

            age = today.year - formatDate.year
    
            if(today.month, today.day) < (formatDate.month, formatDate.day):
                age -= 1
            print("You are " + str(age) + " years old")
            break
        except:
            print("Wrong format (Try YYYY-MM-DD): ")

calculate_age()