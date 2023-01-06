CUSTOMERS = [
    {
        "id": 1,
        "name": "Flynn Fairwind"
    },
    {
        "id": 2,
        "name": "Sylvanas Windrunner"
    },
    {
        "id": 3,
        "name": "Mathias Shaw"
    },
    {
        "id": 4,
        "name": "Anduin Wrynn"
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
