import unittest
import net_state

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(net_state.get_all_interfaces_name())

if __name__ == '__main__':
    unittest.main()
