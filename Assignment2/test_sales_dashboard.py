# This test file checks if some parts of the sales dashboard are working correctly
# You should run this file with: python test_sales_dashboard.py

import unittest
import pandas as pd

# Import your functions and data here
from sales_dashboard import fill_with_mean, total_sales_by_region_and_order_type

# Create a new test case class
class TestSalesDashboard(unittest.TestCase):

    def setUp(self):
        # This runs before every test. We create a small DataFrame to use for testing.
        self.test_df = pd.DataFrame({
            'sales_region': ['East', 'West', 'East'],
            'order_type': ['Retail', 'Wholesale', 'Retail'],
            'quantity': [10, None, 30],
            'unit_price': [2.5, 3.0, None]
        })
        # Create a new column for total price (can contain NaN)
        self.test_df['total_price'] = self.test_df['quantity'] * self.test_df['unit_price']

    def test_fill_with_mean_removes_nans(self):
        # Check if fill_with_mean removes all NaN values
        filled_df = fill_with_mean(self.test_df)
        self.assertFalse(filled_df.isnull().values.any(), "There should be no missing values after fill_with_mean.")

    def test_total_sales_returns_dataframe(self):
        # Set the global df variable so total_sales_by_region_and_order_type can use it
        import sales_dashboard
        sales_dashboard.df = self.test_df.copy()

        result = total_sales_by_region_and_order_type()
        self.assertIsInstance(result, pd.DataFrame, "The result should be a DataFrame.")
        self.assertIn('Retail', result.columns, "The column 'Retail' should be in the result.")

# This runs all the tests when the file is run
if __name__ == '__main__':
    unittest.main()
