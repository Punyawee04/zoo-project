import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid age")

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(55), 150)

    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)
#  Boundary
    def test_y_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_X_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_b_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_a_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_d_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_c_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)   

    def test_f_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()

