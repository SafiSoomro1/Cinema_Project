# cinema with friends gangio

movies = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "Titanic",
    "Avatar",
]

print("Welcome to cinema")
print()

# asking for name and checking for digits in the username n stuff
while True:
    askName = input("Assalam o alaikum gentlemen what are your names!?: ").split()
    capitalized_names = []
    for name in askName:
        capitalized_names.append(name.capitalize())
    askName = capitalized_names
# ----------------------------------------------------------------------------- #
    if len(askName) < 2:
        print("Please enter both of your names!")
        continue
    badName = False
    for name in askName:
        if not name.isalpha():
            print("tera baap elon musk hai? apna naam bata jaldi")
            badName = True
            break
    if not badName:
        break

print(f"Welcome to nueplex!")

for name in askName:
    print("-", name)

# checking movie list and deciding stuff!

MovieList = input("Check movies available?: (Y/N): ").lower()
i = 1
for movieLists in movies:
    if MovieList == "y" or MovieList == "yes":
        print(f"{i}, {movieLists}")
        i += 1
quit_program = False
while True:
    if MovieList == "n" or MovieList == "no":
        Exit = input("Choose a movie or get tf out (Q TO GTFO / C to continue!) ").lower()
        if Exit == "c" or Exit == "continue":
            MovieList = input("Check movies available?: (Y/N): ").lower()
            i = 1
            for movieLists in movies:
                if MovieList == "y" or MovieList == "yes":
                    print(f"{i}, {movieLists}")
                    i += 1
                    quit_program = False
        elif Exit == "q" or Exit == "quit":
            print("Fuck outta here!")
            quit_program = True
            break
        else:
            print("Invalid option!")
    else:
        break


# selecting the movie to watch n shi
if not quit_program:
    while True:
        choice = input("Pick a movie by number: ")

        if choice.isalpha():
            print("Cant enter alphabets!")
            continue

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(movies):
                print("You chose:", movies[choice - 1])
                break
            else:
                print(f"Movie {choice} isn't available!")
                continue
        else:
            print("Invalid input!")
            continue

