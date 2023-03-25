import unittest
def fuel_calculation(mass: int) -> int:
    return (mass // 3) -2


class TestFuelCalculation(unittest.TestCase):
    def test_fuel_calculation(self):
        self.assertEqual(fuel_calculation(12), 2)
        self.assertEqual(fuel_calculation(14), 2)
        self.assertEqual(fuel_calculation(1969), 654)
        self.assertEqual(fuel_calculation(100756), 33583)

class TesttotalfuelRequirement(unittest.TestCase):
    def test_total_fuel_requirement(self):
        modules = [12, 14, 1969, 100756]
        self.assertEqual(sum(fuel_calculation(module) for module in modules) , 34241)


if __name__ == "__main__":

    unittest.main()

  