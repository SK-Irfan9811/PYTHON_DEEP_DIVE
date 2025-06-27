class Manager:
    def __enter__(self):
        print("entered..")
        raise Exception("Exception in enter block")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        return True


# with Manager() as m:
#     print("In progress")
#     raise Exception("For fun")
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setup")
    yield
    print("Cleanup")
with my_context() as m:
    print("Operation")