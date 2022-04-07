class Movies:

    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine


    def display(self):
        print("Movie name =", self.title)
        print("Movie Hero =",self.hero)
        print("Movie Heroine =",self.heroine)

Movies_list=[]
while True:
    title = input("enter movie name")
    hero =  input("enter hero name")
    heroine = input("enter heroine name")
    m=Movies(title,hero,heroine)
    Movies_list.append(m)
    print("moies added successfully")
    option= input("Do you want to add another movie[YES/NO]")
    if option.lower() == "no":
        break
print("all movies info")
print()

for Movies in Movies_list:
    Movies.display()

