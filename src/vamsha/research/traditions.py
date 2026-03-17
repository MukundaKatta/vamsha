"""FamilyTraditions tracking customs/festivals/recipes by lineage."""
from __future__ import annotations
from ..models import FamilyTradition


class FamilyTraditions:
    """Track and manage family traditions across generations."""

    def __init__(self) -> None:
        self._traditions: list[FamilyTradition] = []

    def add_tradition(self, name: str, category: str, description: str,
                      origin: str = "", frequency: str = "") -> FamilyTradition:
        t = FamilyTradition(name=name, category=category, description=description,
                           origin=origin, frequency=frequency)
        self._traditions.append(t)
        return t

    def get_all(self) -> list[FamilyTradition]:
        return self._traditions

    def get_by_category(self, category: str) -> list[FamilyTradition]:
        return [t for t in self._traditions if t.category == category]

    def search(self, query: str) -> list[FamilyTradition]:
        q = query.lower()
        return [t for t in self._traditions if q in t.name.lower() or q in t.description.lower()]

    def remove(self, name: str) -> bool:
        for i, t in enumerate(self._traditions):
            if t.name == name:
                self._traditions.pop(i)
                return True
        return False

    def get_sample_traditions(self) -> list[FamilyTradition]:
        """Return sample traditions common to many Indian families."""
        return [
            FamilyTradition(name="Annual Shraddha", category="ritual", description="Yearly ceremony honoring departed ancestors with food offerings and prayers", frequency="yearly"),
            FamilyTradition(name="Kula Devata Puja", category="ritual", description="Worship of the family deity at the ancestral temple", frequency="yearly"),
            FamilyTradition(name="Family Satyanarayan Katha", category="ritual", description="Family gathering for Satyanarayan Puja on full moon", frequency="monthly"),
            FamilyTradition(name="Grandmother's Special Laddoo Recipe", category="recipe", description="Secret family recipe passed down through generations", frequency="festivals"),
            FamilyTradition(name="Diwali Family Gathering", category="festival", description="All family members gather at the ancestral home for Diwali", frequency="yearly"),
            FamilyTradition(name="New Year Elders' Blessing", category="custom", description="Youngest members touch feet of all elders on New Year day", frequency="yearly"),
            FamilyTradition(name="Wedding Haldi Ceremony", category="custom", description="Family-specific haldi rituals unique to the lineage", frequency="as needed"),
        ]
