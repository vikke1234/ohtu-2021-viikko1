import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_take_empty(self):
        self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_take_negative(self):
        n = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(n, 0)

    def test_take_too_much(self):
        self.varasto.lisaa_varastoon(3)
        n = self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(n, 3)

    def test_add_negative(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_add_too_much(self):
        self.varasto.lisaa_varastoon(1000000000)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_create_negative_space(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_create_negative_items(self):
        v = Varasto(1, -1)
        self.assertAlmostEqual(v.saldo, 0)

    def test_create_too_large(self):
        v = Varasto(1, 2)
        self.assertAlmostEqual(v.saldo, 1)

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
