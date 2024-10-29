class pakistan():
    def capital(self):
        print("the capital of pakistan is islamabad")
    def language(self):
        print("urdu is the most common language in pakistan")
    def type(self):
        print("pakistan is an undeveloped country")
class usa():
    def capital(self):
        print("the capital of USA is washington D.C.")
    def language(self):
        print("english is the most common language in USA")
    def type(self):
        print("USA is a developed country")
objpak = pakistan()
objusa = usa()
for country in(objpak, objusa):
    country.capital()
    country.language()
    country.type()