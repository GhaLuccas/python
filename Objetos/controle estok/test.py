from controle_estoque import Product, Stok
import unittest

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("laptop", 4000.00, 5)
        self.assertEqual(product.name, "laptop")
        self.assertEqual(product.price, 4000.00)
        self.assertEqual(product.quant, 5)
        
class TestStok(unittest.TestCase):
    def setUp(self):
        self.stok = Stok("Estoque Teste")

    def test_add_product(self):
        self.stok.add_product("tablet", 1500.00, 10)
        self.assertTrue("tablet" in self.stok.products)

    def test_remove_product(self):
        self.stok.add_product("tablet", 1500.00, 10)
        self.stok.remove_product("tablet")
        self.assertFalse("tablet" in self.stok.products)

    def test_update_quantity(self):
        self.stok.add_product("tablet", 1500.00, 10)
        self.stok.update_item_quantity("tablet", 15)
        self.assertEqual(self.stok.products["tablet"].quant, 15)

if __name__ == '__main__':
    unittest.main()
