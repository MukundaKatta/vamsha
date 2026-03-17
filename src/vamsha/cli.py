"""CLI for Vamsha."""
from __future__ import annotations
import click
from rich.console import Console
from .research.gotra import GotraDatabase
from .report import VamshaReport

console = Console()


@click.group()
def cli() -> None:
    """Vamsha - Indian Genealogy Tracker."""
    pass


@cli.command()
def list_gotras() -> None:
    """List all gotras."""
    db = GotraDatabase()
    report = VamshaReport()
    report.display_gotra_list(db.get_all_gotras())


@cli.command()
@click.argument("name")
def gotra(name: str) -> None:
    """Show gotra details."""
    db = GotraDatabase()
    report = VamshaReport()
    g = db.get_gotra(name)
    if g:
        report.display_gotra(g)
    else:
        results = db.search_gotras(name)
        if results:
            report.display_gotra(results[0])
        else:
            console.print(f"[red]Gotra not found: {name}[/red]")


@cli.command()
@click.argument("query")
def search_gotra(query: str) -> None:
    """Search gotras."""
    db = GotraDatabase()
    report = VamshaReport()
    results = db.search_gotras(query)
    if results:
        report.display_gotra_list(results)
    else:
        console.print(f"[yellow]No gotras found for: {query}[/yellow]")


@cli.command()
def demo_tree() -> None:
    """Show a demo family tree."""
    from .tree.builder import FamilyTreeBuilder
    from .tree.visualizer import TreeVisualizer
    from .models import Gender

    builder = FamilyTreeBuilder("Demo Family")
    gf = builder.add_person("Raman Sharma", Gender.MALE, 1930, 2010, "Varanasi", "Bharadvaja")
    gm = builder.add_person("Savitri Sharma", Gender.FEMALE, 1935, 2015, "Allahabad")
    builder.add_spouse(gf.id, gm.id, 1955)

    f = builder.add_person("Suresh Sharma", Gender.MALE, 1958, birth_place="Varanasi", gotra="Bharadvaja")
    m = builder.add_person("Kamala Sharma", Gender.FEMALE, 1962, birth_place="Lucknow")
    builder.add_parent_child(gf.id, f.id)
    builder.add_parent_child(gm.id, f.id)
    builder.add_spouse(f.id, m.id, 1982)

    c1 = builder.add_person("Amit Sharma", Gender.MALE, 1985, birth_place="Delhi", gotra="Bharadvaja")
    c2 = builder.add_person("Priya Sharma", Gender.FEMALE, 1988, birth_place="Delhi")
    builder.add_parent_child(f.id, c1.id)
    builder.add_parent_child(m.id, c1.id)
    builder.add_parent_child(f.id, c2.id)
    builder.add_parent_child(m.id, c2.id)
    builder.add_sibling(c1.id, c2.id)

    viz = TreeVisualizer(builder.tree)
    report = VamshaReport()
    tree_str = viz.render_tree(gf.id)
    report.display_tree_ascii(tree_str)

    stats = viz.get_statistics()
    console.print(f"\n[bold]Statistics:[/bold] {stats['total_persons']} persons, {stats['unique_gotras']} gotras")


if __name__ == "__main__":
    cli()
