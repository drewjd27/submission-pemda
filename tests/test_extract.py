import unittest
from unittest.mock import patch, MagicMock
from utils.extract import fetch_products_from_url

class TestExtract(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_fetch_products_from_url_success(self, mock_get):
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Product Test</h3>
                    <div class="price-container">$25</div>
                    <p>Rating: 5 stars</p>
                    <p>Colors: Black, White</p>
                    <p>Size: S, XL</p>
                    <p>Gender: Men</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        result = fetch_products_from_url(url)

        self.assertIsInstance(result, list)  # Memastikan hasil adalah list
        self.assertGreater(len(result), 0)  # Memastikan ada produk yang ditemukan
        self.assertIn('title', result[0])  # Memastikan ada key 'title' dalam produk
        self.assertEqual(result[0]['title'], 'Product Test')  # Memastikan title sesuai

    @patch('utils.extract.requests.get')
    def test_fetch_products_from_url_failure(self, mock_get):
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Client Error")
        mock_get.return_value = mock_response

        # Memastikan fungsi mengeluarkan error saat gagal mengambil data
        with self.assertRaises(RuntimeError) as context:
            fetch_products_from_url(url)
        self.assertIn("Gagal mengambil data", str(context.exception))

    @patch('utils.extract.fetch_products_from_url')
    def test_collect_all_products(self, mock_fetch):
        mock_fetch.return_value = [{'title': 'Product', 'price': '50000', 'rating': '5', 'colors': '3', 'size': 'S', 'gender': 'Women'}]
    
        from utils.extract import collect_all_products
        result = collect_all_products(max_pages=3)
    
        self.assertEqual(len(result), 3)  # Memastikan jumlah produk yang dikumpulkan sesuai dengan jumlah halaman
        self.assertEqual(mock_fetch.call_count, 3)



if __name__ == '__main__':
    unittest.main()
