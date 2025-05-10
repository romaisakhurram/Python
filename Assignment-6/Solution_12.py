
class TemperatureConverter:


    @staticmethod
    def celsius_to_fahrenheit(f):
        return (f * 9/5) + 32

print(f"{TemperatureConverter.celsius_to_fahrenheit(20)} Fahrenheit")
