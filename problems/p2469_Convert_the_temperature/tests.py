import unittest
from p2469_Convert_the_temperature import solution

class TestTemperatureConversion(unittest.TestCase):

    def test_positive_temperature(self):
        self.assertEqual(solution.Temp_convert(122.11), ['395.26000', '251.79800'])

    def test_zero_temperature(self):
        self.assertEqual(solution.Temp_convert(0), ['273.15000', '32.00000'])

    def test_negative_temperature(self):
        self.assertEqual(solution.Temp_convert(-40), ['233.15000', '-40.00000'])

    def test_boiling_point(self):
        self.assertEqual(solution.Temp_convert(100), ['373.15000', '212.00000'])

    def test_freezing_point(self):
        self.assertEqual(solution.Temp_convert(0), ['273.15000', '32.00000'])

    def test_extremely_high_temperature(self):
        self.assertEqual(solution.Temp_convert(1000), ['1273.15000', '1832.00000'])

    def test_extremely_low_temperature(self):
        self.assertEqual(solution.Temp_convert(-273.15), ['0.00000', '-459.67000'])

    def test_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(25.5), ['298.65000', '77.90000'])

    def test_small_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(0.0001), ['273.15010', '32.00018'])

    def test_large_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(123.456789), ['396.60679', '254.22222'])

    def test_negative_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(-0.0001), ['273.14990', '31.99982'])

    def test_near_absolute_zero(self):
        self.assertEqual(solution.Temp_convert(-273.14), ['0.01000', '-459.65200'])

    def test_high_positive_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(999.9999), ['1273.14990', '1831.99982'])

    def test_high_negative_fractional_temperature(self):
        self.assertEqual(solution.Temp_convert(-999.9999), ['-726.84990', '-1767.99982'])

    def test_very_small_positive_temperature(self):
        self.assertEqual(solution.Temp_convert(1e-10), ['273.15000', '32.00000'])

    def test_very_small_negative_temperature(self):
        self.assertEqual(solution.Temp_convert(-1e-10), ['273.15000', '32.00000'])

if __name__ == '__main__':
    unittest.main()