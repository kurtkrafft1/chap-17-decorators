def sort_by_name(data_func):
    def sort_name_add( *args, **kwargs):
        line = data_func(*args)
        return f"{line} ORDER BY last_name ASC, first_name ASC"
    return sort_name_add

class Queries:

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"

queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())
