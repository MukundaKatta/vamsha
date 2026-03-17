"""TreeNavigator finding ancestors/descendants/relatives."""
from __future__ import annotations
from ..models import FamilyTree, Person, Relationship, RelationType


class TreeNavigator:
    """Navigate through the family tree to find relatives."""

    def __init__(self, tree: FamilyTree) -> None:
        self.tree = tree

    def _get_related(self, person_id: str, rel_type: RelationType) -> list[Person]:
        """Get all persons related by a specific type."""
        related_ids = [
            r.person2_id for r in self.tree.relationships
            if r.person1_id == person_id and r.relation_type == rel_type
        ]
        return [self.tree.persons[pid] for pid in related_ids if pid in self.tree.persons]

    def get_parents(self, person_id: str) -> list[Person]:
        return self._get_related(person_id, RelationType.CHILD)

    def get_children(self, person_id: str) -> list[Person]:
        return self._get_related(person_id, RelationType.PARENT)

    def get_spouse(self, person_id: str) -> list[Person]:
        return self._get_related(person_id, RelationType.SPOUSE)

    def get_siblings(self, person_id: str) -> list[Person]:
        return self._get_related(person_id, RelationType.SIBLING)

    def get_grandparents(self, person_id: str) -> list[Person]:
        grandparents = []
        for parent in self.get_parents(person_id):
            grandparents.extend(self.get_parents(parent.id))
        return grandparents

    def get_grandchildren(self, person_id: str) -> list[Person]:
        grandchildren = []
        for child in self.get_children(person_id):
            grandchildren.extend(self.get_children(child.id))
        return grandchildren

    def get_ancestors(self, person_id: str, max_depth: int = 10) -> list[Person]:
        """Get all ancestors up to a given depth."""
        ancestors: list[Person] = []
        visited: set[str] = set()

        def _collect(pid: str, depth: int) -> None:
            if depth > max_depth or pid in visited:
                return
            visited.add(pid)
            parents = self.get_parents(pid)
            for p in parents:
                if p.id not in visited:
                    ancestors.append(p)
                    _collect(p.id, depth + 1)

        _collect(person_id, 0)
        return ancestors

    def get_descendants(self, person_id: str, max_depth: int = 10) -> list[Person]:
        """Get all descendants up to a given depth."""
        descendants: list[Person] = []
        visited: set[str] = set()

        def _collect(pid: str, depth: int) -> None:
            if depth > max_depth or pid in visited:
                return
            visited.add(pid)
            children = self.get_children(pid)
            for c in children:
                if c.id not in visited:
                    descendants.append(c)
                    _collect(c.id, depth + 1)

        _collect(person_id, 0)
        return descendants

    def get_uncles_aunts(self, person_id: str) -> list[Person]:
        """Get uncles and aunts (parents' siblings)."""
        result = []
        for parent in self.get_parents(person_id):
            siblings = self.get_siblings(parent.id)
            result.extend(siblings)
        return result

    def get_cousins(self, person_id: str) -> list[Person]:
        """Get cousins (children of parents' siblings)."""
        cousins = []
        for uncle_aunt in self.get_uncles_aunts(person_id):
            cousins.extend(self.get_children(uncle_aunt.id))
        return cousins

    def find_relationship(self, person1_id: str, person2_id: str) -> str:
        """Find the relationship between two persons (simple BFS)."""
        if person1_id == person2_id:
            return "same person"
        # Direct relationships
        for r in self.tree.relationships:
            if r.person1_id == person1_id and r.person2_id == person2_id:
                if r.relation_type == RelationType.PARENT:
                    child = self.tree.persons.get(person2_id)
                    return "son" if child and child.gender.value == "male" else "daughter"
                elif r.relation_type == RelationType.CHILD:
                    parent = self.tree.persons.get(person2_id)
                    return "father" if parent and parent.gender.value == "male" else "mother"
                elif r.relation_type == RelationType.SPOUSE:
                    spouse = self.tree.persons.get(person2_id)
                    return "husband" if spouse and spouse.gender.value == "male" else "wife"
                elif r.relation_type == RelationType.SIBLING:
                    sib = self.tree.persons.get(person2_id)
                    return "brother" if sib and sib.gender.value == "male" else "sister"
        # Check for grandparent
        gps = self.get_grandparents(person1_id)
        if any(gp.id == person2_id for gp in gps):
            gp = self.tree.persons.get(person2_id)
            return "grandfather" if gp and gp.gender.value == "male" else "grandmother"
        return "relative"

    def get_generation(self, person_id: str) -> int:
        """Compute generation number (0 for roots)."""
        parents = self.get_parents(person_id)
        if not parents:
            return 0
        return 1 + min(self.get_generation(p.id) for p in parents)
