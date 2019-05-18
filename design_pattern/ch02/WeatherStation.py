from WeatherData import WeatherData
from CurrentConditions import CurrentConditions
from Statistics import Statistics
from Forecast import Forecast

def main():
    weatherData = WeatherData()

    currentConditionsDisplay = CurrentConditions(weatherData)
    statisticsDisplay = Statistics(weatherData)
    forecastDisplay = Forecast(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)

if __name__ == "__main__":
    main()
