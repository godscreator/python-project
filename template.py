class template_room:
    def __init__(self):
        self._hotel_name = {"options":{},"help":""}
        self._room_no = {"options":{},"help":""}
        self.no_of_adults = {"options" : {},"help" :"Enter number of adults . It should be a number."}
        self.no_of_children = {"options" : {},"help" : "Enter number of children . It should be a number."}
        self.type = {"options" : {"Deluxe room":"Deluxe room","Club room":"Club room","Executive room":"Executive room","Junior suite":"Junior suite","Suite":"Suite"},"help" : ""}
        self.size = {"options" : {"25x25 ft sq.":"25x25 ft sq.","50x50 ft sq.":"50x50 ft sq."},"help" : ""}
        self.price = {"options":{},"help":""}
        self.beds = {"options":{},"help":""}
        self.bathroom = {"options" : {"private (per room)":"private (per room)","common (per floor)":"common (per floor)"},"help" : ""}
        self.air_conditioning = {"options" : {"AC":"AC","thermostat":"thermostat"},"help" : ""}
        self.internet = {"options" : {"free wifi":"free wifi","wifi (charges applicable)":"wifi (charges applicable)"},"help":""}
        self.entertainment = {"options" : {"Television":"Television","Gaming consoles":"Gaming consoles"},"help" : ""}
        self.housekeeping = {"options" : {"Daily":"Daily","every two days":"every two days","self":"self"},"help" : ""}

class template_hotel:
    def __init__(self):
        self._rooms = {"options":{},"help":""}
        self._room_nos = {"options":{},"help":""}
        self.name ={"options":{},"help":""}
        self.location = {"options":{},"help":""}
        self.type = {"options" : {"Resort":"Resort","Villa":"Villa","Hostel":"Hostel","Service apartment":"Service apartment","Hotel":"Hotel","Lodge":"Lodge","Homestay":"Homestay","Bungalow":"Bungalow","Guest house":"Guest house"},"help" : ""}
        self.meal = {"options" : {"Breakfast included":"Breakfast included","Half board":"Half board","Self catering":"Self catering"},"help" : ""}
        self.reservation_policy = {"options" : {"free cancellation":"free cancellation","Book without credit card":"Book without credit card","no prepayment":"no prepayment"},"help" : ""}
        self.property_details = {"options":{},"help":""}
        self.area_details = {"options" : {"near market":"near market"},"help" : ""}
        
    
