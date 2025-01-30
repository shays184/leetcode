
class solution:

    def Temp_convert(Celsius):
        Kelvin = Celsius + 273.15
        Fahrenheit = Celsius * 1.80 + 32.00
        formatted_kelvin = format(Kelvin,".5f")
        formatted_fahrenheit = format(Fahrenheit,".5f")
        ans = [formatted_kelvin, formatted_fahrenheit]
        return ans

    print (Temp_convert(122.11))
