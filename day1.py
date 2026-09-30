myFilms = ["The Princess Bride", "The Sound of Music", "Midnight Run"]
#print(myFilms)
for film in myFilms:
    print(film)

# add a film
# get another film from the user
addFilm = input("Please enter another film: ")
# add the film to the list
if addFilm in myFilms:
    print("Fool! You already have that film in your list")
else:
    myFilms.append(addFilm)

while True:
    moreFilms = input("Would you like to add another film? (y/n): ")
    if moreFilms.lower() == "y":
        addFilm = input("Please enter another film: ")
        if addFilm in myFilms:
            print("Fool! You already have that film in your list")
        else:
            myFilms.append(addFilm)
    else:
        break

for film in myFilms:
    print(film)
