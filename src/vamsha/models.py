"""Pydantic models for Vamsha."""
from __future__ import annotations
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
import uuid


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class RelationType(str, Enum):
    PARENT = "parent"
    CHILD = "child"
    SPOUSE = "spouse"
    SIBLING = "sibling"


class Gotra(BaseModel):
    name: str
    rishi: str
    pravara: list[str] = Field(default_factory=list)
    veda: str = ""
    sutra: str = ""
    origin: str = ""
    description: str = ""


class Person(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str
    birth_name: str = ""
    gender: Gender = Gender.MALE
    birth_year: int | None = None
    death_year: int | None = None
    birth_place: str = ""
    gotra: str = ""
    occupation: str = ""
    notes: str = ""


class Relationship(BaseModel):
    person1_id: str
    person2_id: str
    relation_type: RelationType
    marriage_year: int | None = None


class FamilyTree(BaseModel):
    name: str = "My Family"
    persons: dict[str, Person] = Field(default_factory=dict)
    relationships: list[Relationship] = Field(default_factory=list)


class FamilyTradition(BaseModel):
    name: str
    category: str  # festival, recipe, custom, ritual
    description: str
    origin: str = ""
    frequency: str = ""
    family_id: str = ""


class TimelineEvent(BaseModel):
    year: int
    person_name: str
    event: str
    description: str = ""
