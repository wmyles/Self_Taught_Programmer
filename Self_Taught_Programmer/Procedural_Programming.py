# this is procedural programming

rock=[]
country=[]
def collect_songs():
    song="enter a song."
    ask="type r or c. q to quit"


    while True:
        genre=input(ask)
        if genre=="q":
            break

        if genre=="r":
            rk=input(song)
            rock.append(rk)
        elif genre=="c":
            cy=input(song)
            country.append(cy)
        else:
            print("Invalid")
    print(rock)
    print(country)
collect_songs()
