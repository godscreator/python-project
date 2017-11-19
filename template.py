def ingen(ops =[],help=""):
    return {"options":ops,"vals":ops,"help":help}
class template_room:
    def __init__(self):
        self._hotelid           = ingen()
        self._roomid            = ingen()
        self.no_of_adults       = ingen(help="Enter number of adults . It should be a number.")
        self.no_of_children     = ingen(help="Enter number of children . It should be a number.")
        self.type               = ingen(ops=["Deluxe room","Club room","Executive room","Junior suite","Suite"])
        self.size               = ingen(ops=["25x25 sq. ft.","50x50 sq. ft."])
        self.price              = ingen()
        self.beds               = ingen()
        self.bathroom           = ingen(ops=["private (per room)","common (per floor)"])
        self.air_conditioning   = ingen(ops=["AC","thermostat"])
        self.internet           = ingen(ops=["free wifi","wifi (charges applicable)"])
        self.entertainment      = ingen(ops=["Television","Gaming consoles"])
        self.housekeeping       = ingen(ops=["Daily","every two days","self"])

class template_hotel:
    def __init__(self):
        self._rooms             = ingen()
        self._roomids           = ingen()
        self.name               = ingen()
        self.location           = ingen()
        self.type               = ingen(ops=["Resort","Villa","Hostel","Service apartment","Hotel",
                                             "Lodge","Homestay","Bungalow","Guest house"])
        self.meal               = ingen(ops=["Breakfast included","Half board","Self catering"])
        self.reservation_policy = ingen(ops=["free cancellation","Book without credit card","no prepayment"])
        self.property_details   = ingen()
        self.area_details       = ingen(ops=["near market"])
        
    
