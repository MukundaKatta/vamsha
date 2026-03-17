"""FamilyTimeline plotting generational history."""
from __future__ import annotations
from ..models import FamilyTree, Person, TimelineEvent
from ..tree.navigator import TreeNavigator


class FamilyTimeline:
    """Plot generational history as a timeline."""

    def __init__(self, tree: FamilyTree) -> None:
        self.tree = tree
        self.nav = TreeNavigator(tree)
        self._custom_events: list[TimelineEvent] = []

    def add_event(self, year: int, person_name: str, event: str, description: str = "") -> None:
        self._custom_events.append(TimelineEvent(year=year, person_name=person_name, event=event, description=description))

    def generate_timeline(self) -> list[TimelineEvent]:
        """Generate a chronological timeline from family data."""
        events: list[TimelineEvent] = []
        for person in self.tree.persons.values():
            if person.birth_year:
                events.append(TimelineEvent(year=person.birth_year, person_name=person.name, event="born", description=f"Born in {person.birth_place}" if person.birth_place else "Born"))
            if person.death_year:
                events.append(TimelineEvent(year=person.death_year, person_name=person.name, event="passed away"))
        # Add marriage events
        seen_marriages: set[str] = set()
        from ..models import RelationType
        for rel in self.tree.relationships:
            if rel.relation_type == RelationType.SPOUSE and rel.marriage_year:
                key = tuple(sorted([rel.person1_id, rel.person2_id]))
                key_str = f"{key[0]}-{key[1]}"
                if key_str not in seen_marriages:
                    seen_marriages.add(key_str)
                    p1 = self.tree.persons.get(rel.person1_id)
                    p2 = self.tree.persons.get(rel.person2_id)
                    if p1 and p2:
                        events.append(TimelineEvent(year=rel.marriage_year, person_name=f"{p1.name} & {p2.name}", event="married"))
        # Add custom events
        events.extend(self._custom_events)
        events.sort(key=lambda e: e.year)
        return events

    def get_generation_spans(self) -> list[dict]:
        """Compute generational spans."""
        generations: dict[int, list[Person]] = {}
        for person in self.tree.persons.values():
            gen = self.nav.get_generation(person.id)
            generations.setdefault(gen, []).append(person)

        spans = []
        for gen_num in sorted(generations.keys()):
            persons = generations[gen_num]
            birth_years = [p.birth_year for p in persons if p.birth_year]
            spans.append({
                "generation": gen_num,
                "count": len(persons),
                "names": [p.name for p in persons],
                "earliest_birth": min(birth_years) if birth_years else None,
                "latest_birth": max(birth_years) if birth_years else None,
            })
        return spans

    def render_timeline_ascii(self) -> str:
        """Render timeline as ASCII."""
        events = self.generate_timeline()
        if not events:
            return "No events to display."
        lines = ["=== Family Timeline ===", ""]
        for event in events:
            marker = "*"
            desc = f" - {event.description}" if event.description else ""
            lines.append(f"  {event.year}  {marker}  {event.person_name}: {event.event}{desc}")
        lines.append("")
        lines.append(f"Total events: {len(events)}")
        return "\n".join(lines)
