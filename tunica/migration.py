import abc

import tunica


class Operation(abc.ABC):
    """Abstract operation"""

    @abc.abstractmethod
    def up(self):
        pass

    @abc.abstractmethod
    def down(self):
        pass


class CreateTable(Operation):
    _name: str
    _columns: list[tunica.Field]

    def __init__(self, name: str, columns: list[tunica.Field]):
        self._name = name
        self._columns = columns

    def up(self):
        pass

    def down(self):
        pass


class Migration:
    """Base migration for all migrations"""

    operations: list[Operation] = []

    def up(self):
        for operation in self.operations:
            operation.up()

    def down(self):
        for operation in self.operations:
            operation.down()
