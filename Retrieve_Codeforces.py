#This snippet of code Retrieves data of contests from the file 'codechef.txt' stored on the local system and arranges it in form
#of a list dictionaries where each dictionary corresponds to a single contest.

contest_list = []

with open('codeforces.txt','r') as f:
    flag = 1
    while True:
        name = f.readline()
        #print('code')
        #print(code)
        if name=="":
            #print('came inside')
            flag=0
            break

        blank = f.readline()
        blank = f.readline()
        
        start = f.readline()
        
        blank = f.readline()
        blank = f.readline()
        blank = f.readline()
        blank = f.readline()
        
        if flag == 1:
            link = 'codeforces.com/contests/'
            code = 'NA'
            contest_detail = {
                          'contest_code' : code,
                          'contest_link' : link,
                          'contest_name' : name,
                          'contest_start' : start
                          }
            contest_list.append(contest_detail.copy())



for contest in contest_list:
    for det in contest:
        print (det,end=' '), print(contest[det])
    print("\n")
















        
