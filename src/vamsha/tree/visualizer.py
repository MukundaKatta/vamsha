"""TreeVisualizer rendering ASCII family trees."""
from __future__ import annotations
from ..models import FamilyTree, Person
from .navigator import TreeNavigator


class TreeVisualizer:
    """Render ASCII family trees."""

    def __init__(self, tree: FamilyTree) -> None:
        self.tree = tree
        self.nav = TreeNavigator(tree)

    def render_tree(self, root_id: str, max_depth: int = 5) -> str:
        """Render family tree as ASCII art starting from a root person."""
        lines: list[str] = []
        self._render_person(root_id, lines, "", True, max_depth, 0, set())
        return "\n".join(lines)

    def _render_person(self, person_id: str, lines: list[str],
                       prefix: str, is_last: bool, max_depth: int,
                       depth: int, visited: set[str]) -> None:
        if depth > max_depth or person_id in visited:
            return
        visited.add(person_id)
        person = self.tree.persons.get(person_id)
        if not person:
            return

        connector = "`-- " if is_last else "|-- "
        if depth == 0:
            connector = ""

        label = self._person_label(person)
        lines.append(f"{prefix}{connector}{label}")

        # Add spouse on same line
        spouses = self.nav.get_spouse(person_id)
        for spouse in spouses:
            if spouse.id not in visited:
                visited.add(spouse.id)
                lines[-1] += f" = {self._person_label(spouse)}"

        # Children
        children = self.nav.get_children(person_id)
        child_prefix = prefix + ("    " if is_last or depth == 0 else "|   ")
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            self._render_person(child.id, lines, child_prefix, is_last_child,
                              max_depth, depth + 1, visited)

    def _person_label(self, person: Person) -> str:
        parts = [person.name]
        if person.birth_year:
            if person.death_year:
                parts.append(f"({person.birth_year}-{person.death_year})")
            else:
                parts.append(f"(b.{person.birth_year})")
        return " ".join(parts)

    def render_ancestors(self, person_id: str) -> str:
        """Render ancestor tree going upward."""
        lines: list[str] = []
        self._render_ancestor(person_id, lines, "", True, 0, set())
        return "\n".join(lines)

    def _render_ancestor(self, person_id: str, lines: list[str],
                         prefix: str, is_last: bool, depth: int,
                         visited: set[str]) -> None:
        if person_id in visited:
            return
        visited.add(person_id)
        person = self.tree.persons.get(person_id)
        if not person:
            return

        connector = "`-- " if is_last else "|-- "
        if depth == 0:
            connector = ""

        lines.append(f"{prefix}{connector}{self._person_label(person)}")

        parents = self.nav.get_parents(person_id)
        parent_prefix = prefix + ("    " if is_last or depth == 0 else "|   ")
        for i, parent in enumerate(parents):
            self._render_ancestor(parent.id, lines, parent_prefix,
                                i == len(parents) - 1, depth + 1, visited)

    def get_statistics(self) -> dict:
        """Get family tree statistics."""
        persons = list(self.tree.persons.values())
        males = sum(1 for p in persons if p.gender.value == "male")
        females = sum(1 for p in persons if p.gender.value == "female")
        birth_years = [p.birth_year for p in persons if p.birth_year]
        gotras = {p.gotra for p in persons if p.gotra}

        return {
            "total_persons": len(persons),
            "males": males,
            "females": females,
            "unique_gotras": len(gotras),
            "gotras": list(gotras),
            "earliest_birth": min(birth_years) if birth_years else None,
            "latest_birth": max(birth_years) if birth_years else None,
            "total_relationships": len(self.tree.relationships) // 2,  # exclude reciprocals
        }
