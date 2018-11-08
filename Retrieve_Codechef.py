#This snippet of code Retrieves data of contests from the file 'codechef.txt' stored on the local system and arranges it in form
#of a list dictionaries where each dictionary corresponds to a single contest and then using post mehtod entire data is parsed to 
#html file where a snippet of code displays this data in form of a html web page




from flask import Flask, render_template
app = Flask(__name__)




contest_list = []

with open('codechef.txt','r') as f:
    flag = 1
    while True:
        code = f.readline()

        
        if code=="":
            flag=0
            break
        link = f.readline()
        #print(link)
        name = f.readline()
        #print(name)
        start = f.readline()
        #print(start)
        end = f.readline()
        #print(end)
        blank = f.readline()
        #print("\n\n")
        if flag == 1:
            contest_detail = {
                          'contest_code' : code,
                          'contest_link' : link,
                          'contest_name' : name,
                          'contest_start' : start,
                          'contest_end' : end
                          }
            contest_list.append(contest_detail.copy())




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', contest_list=contest_list)















        
















        
