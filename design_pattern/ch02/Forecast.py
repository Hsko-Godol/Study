from DisplayElement import DisplayElement

class Forecast(DisplayElement):
    def display(self):
        future_temp = self.temp + 1.0
        if future_temp > 40.0:
            future_temp = 18.0
        future_humidity = self.humidity + 5.0
        if future_humidity > 100.0:
            future_humidity = 0.0
        future_wind_speed = self.wind_speed + 0.5
        if future_wind_speed > 10.0:
            future_wind_speed = 1.0

        print("This is the forecast of the weather")
        print("Temperature :", future_temp, "C")
        print("Humidity :", future_humidity, "%")
        print("Wind Speed :", future_wind_speed, "m/s")
