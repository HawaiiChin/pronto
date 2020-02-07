"""A Python frontend to ontologies.

pronto is a Python agnostic library designed to work with ontologies. At the
moment, it can parse ontologies in the OBO, OBO Graphs or OWL in RDF/XML
format, on either the local host or from an network location, and export
ontologies to OBO or OBO Graphs (in JSON format).

Caution:
    Only classes and modules reachable from the top-level package ``pronto``
    are considered public and are guaranteed stable over `Semantic Versioning
    <https://semver.org/>`_. Use submodules (other than `~pronto.warnings`)
    at your own risk!

Note:
    ``pronto`` implements proper *type checking* for most of the methods and
    properties exposed in the public classes. This reproduces the behaviour
    of the Python standard library, to avoid common errors. This feature does
    however increase overhead, but can be disabled by executing Python in
    optimized mode (with the ``-O`` flag). **The time to parse an OBO file is
    reduced by about 60% in optimized mode.**

"""
from __future__ import annotations

__author__ = "Martin Larralde <martin.larralde@embl.de>"
__license__ = "MIT"
__version__ = (
    __import__("pkg_resources")
    .resource_string(__name__, "_version.txt")
    .decode("utf-8")
    .strip()
)

from .utils import warnings
from .entity import Entity
from .definition import Definition
from .metadata import Metadata, Subset
from .ontology import Ontology
from .pv import LiteralPropertyValue, PropertyValue, ResourcePropertyValue
from .relationship import Relationship, RelationshipData
from .synonym import Synonym, SynonymData, SynonymType
from .term import Term, TermData
from .xref import Xref

__all__ = [
    # modules
    "warnings",
    # classes
    Ontology.__name__,
    Entity.__name__,
    Term.__name__,
    TermData.__name__,
    Metadata.__name__,
    Subset.__name__,
    Definition.__name__,
    Relationship.__name__,
    RelationshipData.__name__,
    Synonym.__name__,
    SynonymData.__name__,
    SynonymType.__name__,
    PropertyValue.__name__,
    LiteralPropertyValue.__name__,
    ResourcePropertyValue.__name__,
    Xref.__name__,
]
