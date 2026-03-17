"""Tests for Vamsha."""
import pytest
from vamsha.tree.builder import FamilyTreeBuilder
from vamsha.tree.navigator import TreeNavigator
from vamsha.tree.visualizer import TreeVisualizer
from vamsha.research.gotra import GotraDatabase
from vamsha.research.traditions import FamilyTraditions
from vamsha.research.timeline import FamilyTimeline
from vamsha.models import Gender, RelationType


class TestGotraDatabase:
    def test_49_plus_gotras(self):
        db = GotraDatabase()
        assert db.get_gotra_count() >= 49

    def test_get_gotra(self):
        db = GotraDatabase()
        g = db.get_gotra("Bharadvaja")
        assert g is not None
        assert g.rishi == "Bharadvaja"
        assert len(g.pravara) >= 3

    def test_search(self):
        db = GotraDatabase()
        results = db.search_gotras("Vashishtha")
        assert len(results) >= 1

    def test_gotras_by_veda(self):
        db = GotraDatabase()
        rig = db.get_gotras_by_veda("Rigveda")
        assert len(rig) >= 10


class TestFamilyTreeBuilder:
    def _build_sample_tree(self):
        builder = FamilyTreeBuilder("Test Family")
        gf = builder.add_person("Grandfather", Gender.MALE, 1940)
        gm = builder.add_person("Grandmother", Gender.FEMALE, 1945)
        builder.add_spouse(gf.id, gm.id, 1965)
        f = builder.add_person("Father", Gender.MALE, 1970)
        builder.add_parent_child(gf.id, f.id)
        builder.add_parent_child(gm.id, f.id)
        m = builder.add_person("Mother", Gender.FEMALE, 1972)
        builder.add_spouse(f.id, m.id, 1995)
        c = builder.add_person("Child", Gender.MALE, 2000)
        builder.add_parent_child(f.id, c.id)
        builder.add_parent_child(m.id, c.id)
        return builder, gf, gm, f, m, c

    def test_add_person(self):
        builder = FamilyTreeBuilder()
        p = builder.add_person("Test", Gender.MALE)
        assert p.name == "Test"
        assert builder.get_family_size() == 1

    def test_add_relationship(self):
        builder, gf, gm, f, m, c = self._build_sample_tree()
        assert builder.get_family_size() == 5

    def test_remove_person(self):
        builder = FamilyTreeBuilder()
        p = builder.add_person("Test", Gender.MALE)
        assert builder.remove_person(p.id)
        assert builder.get_family_size() == 0

    def test_find_by_name(self):
        builder, *_ = self._build_sample_tree()
        results = builder.find_person_by_name("Father")
        assert len(results) == 1


class TestTreeNavigator:
    def _build_tree(self):
        builder = FamilyTreeBuilder()
        gf = builder.add_person("GF", Gender.MALE, 1940)
        gm = builder.add_person("GM", Gender.FEMALE, 1945)
        builder.add_spouse(gf.id, gm.id)
        f = builder.add_person("F", Gender.MALE, 1970)
        builder.add_parent_child(gf.id, f.id)
        builder.add_parent_child(gm.id, f.id)
        m = builder.add_person("M", Gender.FEMALE, 1972)
        builder.add_spouse(f.id, m.id)
        c = builder.add_person("C", Gender.MALE, 2000)
        builder.add_parent_child(f.id, c.id)
        builder.add_parent_child(m.id, c.id)
        return builder.tree, gf, gm, f, m, c

    def test_get_parents(self):
        tree, gf, gm, f, m, c = self._build_tree()
        nav = TreeNavigator(tree)
        parents = nav.get_parents(c.id)
        assert len(parents) == 2

    def test_get_children(self):
        tree, gf, gm, f, m, c = self._build_tree()
        nav = TreeNavigator(tree)
        children = nav.get_children(f.id)
        assert len(children) == 1

    def test_get_grandparents(self):
        tree, gf, gm, f, m, c = self._build_tree()
        nav = TreeNavigator(tree)
        gps = nav.get_grandparents(c.id)
        assert len(gps) == 2

    def test_get_ancestors(self):
        tree, gf, gm, f, m, c = self._build_tree()
        nav = TreeNavigator(tree)
        ancestors = nav.get_ancestors(c.id)
        assert len(ancestors) == 4  # F, M, GF, GM

    def test_get_spouse(self):
        tree, gf, gm, f, m, c = self._build_tree()
        nav = TreeNavigator(tree)
        spouses = nav.get_spouse(f.id)
        assert len(spouses) == 1
        assert spouses[0].name == "M"


class TestTreeVisualizer:
    def test_render(self):
        builder = FamilyTreeBuilder()
        p1 = builder.add_person("Root", Gender.MALE, 1940)
        p2 = builder.add_person("Child", Gender.MALE, 1970)
        builder.add_parent_child(p1.id, p2.id)
        viz = TreeVisualizer(builder.tree)
        output = viz.render_tree(p1.id)
        assert "Root" in output
        assert "Child" in output

    def test_statistics(self):
        builder = FamilyTreeBuilder()
        builder.add_person("P1", Gender.MALE, 1940, gotra="Bharadvaja")
        builder.add_person("P2", Gender.FEMALE, 1945)
        viz = TreeVisualizer(builder.tree)
        stats = viz.get_statistics()
        assert stats["total_persons"] == 2
        assert stats["males"] == 1


class TestFamilyTraditions:
    def test_add_tradition(self):
        ft = FamilyTraditions()
        t = ft.add_tradition("Annual Puja", "ritual", "Yearly family puja")
        assert t.name == "Annual Puja"
        assert len(ft.get_all()) == 1

    def test_sample_traditions(self):
        ft = FamilyTraditions()
        samples = ft.get_sample_traditions()
        assert len(samples) >= 5


class TestFamilyTimeline:
    def test_timeline(self):
        builder = FamilyTreeBuilder()
        p1 = builder.add_person("Elder", Gender.MALE, 1940, 2020)
        p2 = builder.add_person("Young", Gender.MALE, 1970)
        builder.add_parent_child(p1.id, p2.id)
        tl = FamilyTimeline(builder.tree)
        events = tl.generate_timeline()
        assert len(events) >= 3  # 2 births + 1 death

    def test_ascii_render(self):
        builder = FamilyTreeBuilder()
        builder.add_person("Test", Gender.MALE, 1990)
        tl = FamilyTimeline(builder.tree)
        output = tl.render_timeline_ascii()
        assert "1990" in output
