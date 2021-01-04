class pp :
    def __init__(self,ownername,length,hole_it_is_present_in) :
        self.ownername = ownername
        self.length = length # in mm 
        self.hole_it_is_present_in = hole_it_is_present_in

small_pp_person = pp("Samuel Miller",1,"Whitehatjr")
for i in range(small_pp_person.length) :
    print("Hello World")
