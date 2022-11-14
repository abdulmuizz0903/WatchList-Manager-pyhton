import pandas as pd
import numpy as np
import imdb

id = imdb.Cinemagoer()

try:
    MainDF = pd.read_csv("data.csv")
except:
    df = pd.DataFrame({"Series Name":[], "Genre":[], "Total no. of Episodes":[], "Episodes Watched":[], "IMDb Rating":[], "Personal Rating/10":[], "Status":[],"User's Name":[]})
    df.to_csv("data.csv", index=False, mode="w")
    MainDF = pd.read_csv("data.csv")
try:
    userName = MainDF["User's Name"][0]
except:
    userName = None


if userName:
    print(f'Welcome {userName}')
else:
    print("Welcome to our App for the first time\n\n")
    userName = input("What's your Name?\n")

while True:
    print("Whats do you want?\n\n1. To see my data.\n2. To add a new Movie/Series\n3. To add episode to existing Movie/Series\n4. To Change personal rating of existing Movie/Series\n5. To change the Watch Status of Existing Movie/Series\n\nWrite the Number of the command you want to proceed with.\n\n")
    ans0 = input()

    while True:
        if ans0 == "1":
            print(MainDF)
            break
        elif ans0 == "2":
            ans1 = input("Enter the Name of the Movie/Series you want to add:\n")
            items = id.search_movie(ans1)
            for q in range(3):    
                if len(items) == 0:
                    items = id.search_movie(ans1)
                else:
                    break
                
            for q in range(len(items)):
                print(f"{str(q+1)}. {items[q]}")
            print("Here are Some results, which one do you like to add?")
            ans2 = int(input())
            item = id.get_movie(items[ans2-1].movieID)
            if items[ans2-1]['kind'] == 'tv series':
                id.update(item, 'episodes')
                ep = item.data['episodes']
                noep = 0
                for q in ep.keys():
                    noep += len(ep[q])
            else:
                noep = "Its a Movie"
            genre = item['genres'][0]
            name = str(item)
            Irating = item.data['rating']
            status = "Watching"
            if items[ans2-1]['kind'] == 'tv series':
                epw = input("How many episodes of this series have you wactched?\n")
                if int(epw) == int(noep):
                    status = "Completed"
            else:
                epw = "Its a Movie"
            Prating = input("What's Your personal rating for this Movie or Series?")
            MainDF.loc[len(MainDF.index)] = [name, genre, noep, epw, Irating, Prating, status, userName]
            MainDF.to_csv("data.csv", index=False, mode="w")
            print("New Movie/Series added!")
            break
        elif ans0 == "3":
            print("Enter the serial No. of the Series you want to update:(If you dont know the serial number go back by entering 'x' and see your data)\n")
            ans1 = input()
            if ans1 == "x":
                break
            else:
                print(f"How many episodes would you like to add to {MainDF.loc[int(ans1)][0]} ?\n")
                ans2 = int(input())
                MainDF.at[int(ans1), 'Episodes Watched'] = MainDF.at[int(ans1), 'Episodes Watched'] + ans2
                if MainDF.loc[int(ans1)][3] == MainDF.loc[int(ans1)][2]:
                    MainDF.at[int(ans1), 'Status'] = "Completed" 
                print("Episodes Added !")
                break
        elif ans0 == "4":
            print("Enter the serial No. of the Series/Movie you want to update:(If you dont know the serial number go back by entering 'x' and see your data)\n")
            ans1 = input()
            if ans1 == "x":
                break
            else:
                print(f"Whats the new rating for {MainDF.loc[int(ans1)][0]} ?\n")
                ans2 = input()
                MainDF.at[int(ans1), 'Personal Rating/10'] = ans2
                print("Personal Rating Updated!")
                break
        elif ans0 == "5":
            print("Enter the serial No. of the Series/Movie you want to update:(If you dont know the serial number go back by entering 'x' and see your data)\n")
            ans1 = input()
            if ans1 == "x":
                break
            else:
                print(f"Whats the New Staus of  {MainDF.loc[int(ans1)][0]} ?(Choose one of the below)\n")
                print("1. Watching\n2. On Hold\n3. Stopped")
                ans2 = int(input())
                l = ["Watching", "On Hold", "Stopped"]
                MainDF.at[int(ans1), 'Status'] = l[ans2]
                print("Status Updated !")
                break
        else:
                break
    inp = input("Do you want to Exit?(Y/N)\n")
    if inp.lower() == "y":
        MainDF.to_csv("data.csv", index=False, mode="w")
        break
    else:
        continue
        