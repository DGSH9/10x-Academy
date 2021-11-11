class Movie:
    def __init__(self,language,num_characters,length_in_minutes):
        self.language = language
        self.num_characters = num_characters
        self.length_in_minutes = length_in_minutes
    
    def run(self):
        print("This is a " + str(self.language)+ " " + "movie with " + str(self.num_characters)+ " " + "characters and is "+ str(self.length_in_minutes) + " " + "minutes long.")
        # print(self.length_in_minutes)
        # print(self.num_characters)
        # print(self.language)
    
    
obj1 = Movie(input(),int(input()),int(input()))
Movie.run(obj1)