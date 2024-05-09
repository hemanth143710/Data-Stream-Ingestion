class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.slots = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }
        self.initial_slots = self.slots.copy()

    def fuel_vehicle(self, fuel_type):
        if self.slots[fuel_type] > 0:
            self.slots[fuel_type] -= 1
            return True
        else:
            return False

    def open_fuel_slot(self, fuel_type):
        if self.slots[fuel_type] < self.initial_slots[fuel_type]:
            self.slots[fuel_type] += 1
            return True
        else:
            return False


fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print("diesel:",fuel_station.fuel_vehicle("diesel")) 
print("petrol:",fuel_station.fuel_vehicle("petrol")) 
print("diesel:",fuel_station.fuel_vehicle("diesel"))  
print("electric:",fuel_station.fuel_vehicle("electric"))  
print("diesel:",fuel_station.fuel_vehicle("diesel")) 
print("diesel:",fuel_station.open_fuel_slot("diesel"))
print("diesel:",fuel_station.fuel_vehicle("diesel"))  
print("electric:",fuel_station.open_fuel_slot("electric")) 
print("electric:",fuel_station.open_fuel_slot("electric")) 
