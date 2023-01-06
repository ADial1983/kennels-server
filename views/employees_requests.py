EMPLOYEES = [
    {
        "id": 1,
        "name": "Tess Greymane"
    },
    {
        "id": 2,
        "name": "Darion Mograine"
    },
    {
        "id": 3,
        "name": "Jaina Proudmoore"
    },
    {
        "id": 4,
        "name": "Gelbin Mekkatorque"
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
