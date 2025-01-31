
from typing import List


class Solution:

    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        formatted_kelvin = float(format(kelvin,".5f"))
        formatted_fahrenheit = float(format(fahrenheit,".5f"))
        return [formatted_kelvin, formatted_fahrenheit]
