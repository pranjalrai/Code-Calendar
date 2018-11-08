#This snippet of code Retrieves data of contests from the file 'codechef.txt' stored on the local system and arranges it in form
#of a list dictionaries where each dictionary corresponds to a single contest.

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



for contest in contest_list:
    for det in contest:
        print (det,end=' '), print(contest[det])
    print("\n")
















        
