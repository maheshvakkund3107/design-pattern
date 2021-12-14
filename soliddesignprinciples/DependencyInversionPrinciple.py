from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


# Accessing the internals of the low level module relationships in a high level module Research is a bad practice.
class Research:
    def __init__(self, relationships1):
        relations = relationships1.relations
        for i in relations:
            if i[0].name == 'John' and i[1] == Relationship.PARENT:
                print(f"John has a child called {i[2].name}")


# Improved Code
# Goal is to not to depend on the low level functionality directly ,
# we create a abstraction and provide the implementation for the low level module which
# is accessed by the high level module
class RelationShipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class RelationshipsImproved(RelationShipBrowser):
    def find_all_children_of(self, name):
        for i in self.relations:
            if i[0].name == name and i[1] == Relationship.PARENT:
                yield i[2].name

    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class ResearchImproved:
    def __init__(self, browser):
        for i in browser.find_all_children_of('John'):
            print(f"John has a child called {i}")


if __name__ == '__main__':
    person = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")
    relationships1 = Relationships()
    relationships1.add_parent_child(person, child1)
    relationships1.add_parent_child(person, child2)
    relationships2 = RelationshipsImproved()
    relationships2.add_parent_child(person, child1)
    relationships2.add_parent_child(person, child2)
    Research(relationships1)
    ResearchImproved(relationships2)
