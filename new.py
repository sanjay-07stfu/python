# print("Welcome")

# element=[50,60,70,80,90]

# for x in element:
#     print(x)


# print("sanjay yedage")

# array=[10,20,30,40,50]

# for x in array:
#     print(x)




from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def show_date():
    return f"<h2>Today's date is: {date.today()}</h2>"

if __name__ == '__main__':
    app.run()
