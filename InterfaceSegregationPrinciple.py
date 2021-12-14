# This fashion all the classes inheriting from Machine need to inherit all the methods.
# So the idea is to Segregate as per the requirements.
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        # OK
        pass

    def fax(self, document):
        pass  # DO NOTHING

    def scan(self, document):
        raise NotImplementedError  # Or DO Nothing


# Interface Segregating Principle- Example
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def scan(self, document):
        pass

    def print(self, document):
        pass

