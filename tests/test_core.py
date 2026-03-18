"""Tests for Vamsha."""
from src.core import Vamsha
def test_init(): assert Vamsha().get_stats()["ops"] == 0
def test_op(): c = Vamsha(); c.generate(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Vamsha(); [c.generate() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Vamsha(); c.generate(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Vamsha(); r = c.generate(); assert r["service"] == "vamsha"
