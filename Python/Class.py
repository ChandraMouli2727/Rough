'''
                       Class
                       Human
Properties                         Methods
Name                                 Speaks
Gender                              Do Work
Occupation                       Sleeps

object of Class "Human"
'''

class Human:
    def __init__(self,n,G,O):   # it will intialize Properties of class when yiu create instance
        self.name = n
        self.Gender = G
        self.Occupation = O

    def do_work(self):
        if self.Occupation == "tennis player":
            print(self.name,"Play Tennis")
        elif self.Occupation == 'actor':
            print(self.name,"Shoot a film")

    def speaks(self):
        print(self.name," Says How are you ? ")



# Now Create Instance

tom = Human("Tom","Male","actor")
tom.do_work()
tom.speaks()