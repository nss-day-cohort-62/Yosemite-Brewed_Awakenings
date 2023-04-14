EMPLOYEES = [{
    "id": 1,
    "name": "Alphonse Meron",
    "email": "ameron0@mashable.com",
    "hourlyRate": 11.50

}, {
    "id": 2,
    "name": "Damara Pentecust",
    "email": "dpentecust1@apache.org",
    "hourlyRate": 10.75

}, {
    "id": 3,
    "name": "Anna Bowton",
    "email": "abowton2@wisc.edu",
    "hourlyRate": 12.30

}, {
    "id": 4,
    "name": "Hunfredo Drynan",
    "email": "hdrynan3@bizjournals.com",
    "hourlyRate": 12.00

}, {
    "id": 5,
    "name": "Elmira Bick",
    "email": "ebick4@biblegateway.com",
    "hourlyRate": 12.30

}, {
    "id": 6,
    "name": "Bernie Dreger",
    "email": "bdreger5@zimbio.com",
    "hourlyRate": 11.50

}, {
    "id": 7,
    "name": "Rolando Gault",
    "email": "rgault6@google.com",
    "hourlyRate": 11.80

}, {
    "id": 8,
    "name": "Tiffanie Tubby",
    "email": "ttubby7@intel.com",
    "hourlyRate": 21.00

}, {
    "id": 9,
    "name": "Tomlin Cutill",
    "email": "tcutill8@marketwatch.com",
    "hourlyRate": 12.10

}, {
    "id": 10,
    "name": "Arv Biddle",
    "email": "abiddle9@cafepress.com",
    "hourlyRate": 13.00

}]

def get_all_employees():
    '''get all employees'''
    return EMPLOYEES

def get_single_employee(id):
    '''get a single employee'''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    '''create a new employee'''
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def update_employee(id, new_employee):
    '''update employee'''
    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            EMPLOYEES[index] = new_employee
            break

def delete_employee(id):
    '''delete an employee'''
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            employee_index = index
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)
