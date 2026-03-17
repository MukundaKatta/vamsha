"""Report generation for Vamsha."""
from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .models import Person, Gotra, FamilyTradition, TimelineEvent


class VamshaReport:
    def __init__(self) -> None:
        self.console = Console()

    def display_person(self, person: Person) -> None:
        years = ""
        if person.birth_year:
            years = f"b.{person.birth_year}"
            if person.death_year:
                years += f" - d.{person.death_year}"
        self.console.print(Panel(
            f"[bold]{person.name}[/bold] ({person.gender.value})\n"
            f"Years: {years}\nPlace: {person.birth_place}\n"
            f"Gotra: {person.gotra}\nOccupation: {person.occupation}",
            title="Person"))

    def display_gotra(self, gotra: Gotra) -> None:
        self.console.print(Panel(
            f"[bold magenta]{gotra.name}[/bold magenta]\n"
            f"Rishi: {gotra.rishi}\nPravara: {' > '.join(gotra.pravara)}\n"
            f"Veda: {gotra.veda}\nSutra: {gotra.sutra}\n\n{gotra.description}",
            title="Gotra"))

    def display_gotra_list(self, gotras: list[Gotra]) -> None:
        table = Table(title="Gotras")
        table.add_column("Name", style="bold cyan")
        table.add_column("Rishi", style="yellow")
        table.add_column("Pravara")
        table.add_column("Veda")
        for g in gotras:
            table.add_row(g.name, g.rishi, " > ".join(g.pravara[:3]), g.veda)
        self.console.print(table)

    def display_timeline(self, events: list[TimelineEvent]) -> None:
        table = Table(title="Family Timeline")
        table.add_column("Year", style="bold")
        table.add_column("Person", style="cyan")
        table.add_column("Event", style="yellow")
        table.add_column("Details")
        for e in events:
            table.add_row(str(e.year), e.person_name, e.event, e.description)
        self.console.print(table)

    def display_tree_ascii(self, tree_str: str) -> None:
        self.console.print(Panel(tree_str, title="Family Tree"))
