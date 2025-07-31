import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        products = [
            {'title': 'Product 1', 'price': '120000', 'rating': '4.0', 'colors': '3', 'size': 'L', 'gender': 'Men'},
            {'title': 'Product 2', 'price': '150000', 'rating': '5.0', 'colors': '3', 'size': 'M', 'gender': 'Women'}
        ]
        
        df = transform_data(products)
        
        self.assertEqual(len(df), 2)
        self.assertIn('price', df.columns)
        self.assertIn('rating', df.columns)
        self.assertIn('timestamp', df.columns)
        self.assertTrue(df['price'].iloc[0] > 0)
        self.assertTrue(df['rating'].iloc[0] > 0)

    def test_invalid_price(self):
        products = [
            {'title': 'Product 1', 'price': 'invalid_price', 'rating': '4.0', 'colors': '3', 'size': 'L', 'gender': 'Men'}
        ]
        
        df = transform_data(products)
        
        self.assertEqual(len(df), 0)  

    def test_transform_data_with_unknown_product_and_duplicates(self):
        products = [
            {'title': 'Unknown Product', 'price': '120000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Men'},
            {'title': 'Product 1', 'price': '120000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Men'},
            {'title': 'Product 1', 'price': '120000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Men'},  # Baris duplikat
        ]
        df = transform_data(products)
        self.assertEqual(len(df), 1)  # Hanya satu produk yang harus ada setelah menghapus 'Unknown Product' dan duplikat

if __name__ == '__main__':
    unittest.main()