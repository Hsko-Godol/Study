from DisplayElement import DisplayElement

class Statistics(DisplayElement):
    def display(self):
        print("This is the statistics of the weather")

        print("Temperature")
        print("\t- MIN =", self.temp)
        print("\t- AVG =", self.temp)
        print("\t- MAX =", self.temp)

        print("Humidity")
        print("\t- MIN =", self.humidity)
        print("\t- AVG =", self.humidity)
        print("\t- MAX =", self.humidity)

        print("Wind Speed")
        print("\t- MIN =", self.wind_speed)
        print("\t- AVG =", self.wind_speed)
        print("\t- MAX =", self.wind_speed)
