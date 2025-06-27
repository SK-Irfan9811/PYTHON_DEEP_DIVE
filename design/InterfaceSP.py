from abc import abstractmethod, ABC


class TestInterface(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def retry(self):
        pass

    @abstractmethod
    def skip(self):
        pass


class SmokeTests(TestInterface):
    def retry(self):  # violates the ISP
        print("no valid")

    def skip(self):  # violates the ISP
        print("Not valid")

    def run(self):
        print("Running")
# solution is segregate the TestInterface to work in terms of atoms
