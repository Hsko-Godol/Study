from DisplayElement import DisplayElement

class CurrentConditions(DisplayElement):
    def display(self):
        print("This is the current conditions of the weather")
        print("Temperature :", self.temp, "C")
        print("Humidity :", self.humidity, "%")
        print("Wind Speed :", self.wind_speed, "m/s")
