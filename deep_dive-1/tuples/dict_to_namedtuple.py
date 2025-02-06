from collections import namedtuple
from typing import List

entries = [
    {"id": 1, "name": "Write Report", "status": "Pending", "priority": "High", "agreement": "2090"},
    {"id": 2, "name": "Review PR", "priority": "Medium"},
    {"id": 3, "name": "Update Documentation", "status": "Completed", "priority": "Low"},
    {"id": 4, "name": "Prepare Presentation", "status": "Pending", "priority": "High"},
    {"id": 5, "status": "In Progress", "name": "Fix Bug #124"},
]


def convert_to_namedtuples(tasks: List[dict]):
    keys_ = {key for task in tasks for key in task.keys()}
    Task = namedtuple("Task", keys_)
    Task.__new__.__defaults__ = ((None,) * len(Task._fields))
    return [Task(**task) for task in tasks]


for entry in convert_to_namedtuples(entries):
    print(entry)
