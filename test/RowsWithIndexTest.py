from test.StratumTestCase import StratumTestCase


class RowsWithIndexTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type rows_with_index must return multi dimensional array.
        """
        rows = self._dl.tst_test_rows_with_index1(100)
        self.assertIsInstance(rows, dict)
        self.assertIn('a', rows)
        self.assertIn('b', rows['a'])
        self.assertIsInstance(rows['a']['b'], list)
        self.assertEqual(3, len(rows['a']['b']))

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        Stored routine with designation type rows_with_index must return empty array when no rwos are selected.
        """
        rows = self._dl.tst_test_rows_with_index1(0)
        self.assertIsInstance(rows, dict)
        self.assertEqual(0, len(rows))

# ----------------------------------------------------------------------------------------------------------------------
