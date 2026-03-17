"""FamilyTreeBuilder with person/relationship CRUD."""
from __future__ import annotations
from ..models import FamilyTree, Person, Relationship, RelationType, Gender


class FamilyTreeBuilder:
    """Build and manage a family tree with CRUD operations."""

    def __init__(self, name: str = "My Family") -> None:
        self.tree = FamilyTree(name=name)

    def add_person(self, name: str, gender: Gender = Gender.MALE,
                   birth_year: int | None = None, death_year: int | None = None,
                   birth_place: str = "", gotra: str = "", occupation: str = "",
                   notes: str = "", birth_name: str = "") -> Person:
        """Add a person to the family tree."""
        person = Person(name=name, gender=gender, birth_year=birth_year,
                       death_year=death_year, birth_place=birth_place,
                       gotra=gotra, occupation=occupation, notes=notes,
                       birth_name=birth_name)
        self.tree.persons[person.id] = person
        return person

    def remove_person(self, person_id: str) -> bool:
        """Remove a person and their relationships."""
        if person_id not in self.tree.persons:
            return False
        del self.tree.persons[person_id]
        self.tree.relationships = [
            r for r in self.tree.relationships
            if r.person1_id != person_id and r.person2_id != person_id
        ]
        return True

    def update_person(self, person_id: str, **kwargs) -> Person | None:
        """Update person attributes."""
        person = self.tree.persons.get(person_id)
        if not person:
            return None
        for key, value in kwargs.items():
            if hasattr(person, key):
                setattr(person, key, value)
        return person

    def add_relationship(self, person1_id: str, person2_id: str,
                         relation_type: RelationType,
                         marriage_year: int | None = None) -> Relationship | None:
        """Add a relationship between two persons."""
        if person1_id not in self.tree.persons or person2_id not in self.tree.persons:
            return None
        rel = Relationship(person1_id=person1_id, person2_id=person2_id,
                          relation_type=relation_type, marriage_year=marriage_year)
        self.tree.relationships.append(rel)
        # Add reciprocal
        reciprocal_map = {
            RelationType.PARENT: RelationType.CHILD,
            RelationType.CHILD: RelationType.PARENT,
            RelationType.SPOUSE: RelationType.SPOUSE,
            RelationType.SIBLING: RelationType.SIBLING,
        }
        reciprocal = Relationship(person1_id=person2_id, person2_id=person1_id,
                                  relation_type=reciprocal_map[relation_type],
                                  marriage_year=marriage_year)
        self.tree.relationships.append(reciprocal)
        return rel

    def add_parent_child(self, parent_id: str, child_id: str) -> Relationship | None:
        """Convenience method to add parent-child relationship."""
        return self.add_relationship(parent_id, child_id, RelationType.PARENT)

    def add_spouse(self, person1_id: str, person2_id: str,
                   marriage_year: int | None = None) -> Relationship | None:
        """Convenience method to add spousal relationship."""
        return self.add_relationship(person1_id, person2_id, RelationType.SPOUSE, marriage_year)

    def add_sibling(self, person1_id: str, person2_id: str) -> Relationship | None:
        """Convenience method to add sibling relationship."""
        return self.add_relationship(person1_id, person2_id, RelationType.SIBLING)

    def get_person(self, person_id: str) -> Person | None:
        return self.tree.persons.get(person_id)

    def find_person_by_name(self, name: str) -> list[Person]:
        return [p for p in self.tree.persons.values() if name.lower() in p.name.lower()]

    def get_all_persons(self) -> list[Person]:
        return list(self.tree.persons.values())

    def get_relationships(self, person_id: str) -> list[Relationship]:
        return [r for r in self.tree.relationships if r.person1_id == person_id]

    def get_family_size(self) -> int:
        return len(self.tree.persons)
