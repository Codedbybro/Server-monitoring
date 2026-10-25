import unittest

import monitor


class StatusTests(unittest.TestCase):
    def test_status_boundaries(self):
        self.assertEqual(monitor.get_status(69.9), "OK")
        self.assertEqual(monitor.get_status(70), "WARNING")
        self.assertEqual(monitor.get_status(89.9), "WARNING")
        self.assertEqual(monitor.get_status(90), "CRITICAL")

    def test_custom_thresholds(self):
        self.assertEqual(monitor.get_status(50, warning=50, critical=80), "WARNING")
        self.assertEqual(monitor.get_status(80, warning=50, critical=80), "CRITICAL")

    def test_overall_status_uses_worst_state(self):
        self.assertEqual(monitor.get_overall_status(20, 30, 40), "OK")
        self.assertEqual(monitor.get_overall_status(20, 75, 40), "WARNING")
        self.assertEqual(monitor.get_overall_status(20, 75, 91), "CRITICAL")


if __name__ == "__main__":
    unittest.main()
