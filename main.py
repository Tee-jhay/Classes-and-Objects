class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score ):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    print ("Details of new student:")

    def change_name(self, new_name):
        self.name = new_name
        print("The student new name is ", self.name)

    def change_age(self, new_age):
        self.age = new_age
        print("The student new age is ", self.age)    

    def add_track(self, new_track):
        self.tracks = self.tracks.append(...)
        print("The student new track is ", self.tracks)

    def get_score(self):
        print("The student new score is ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
