class OldSystem:
    def do_old_operation(self):
        return "Old System Operation"

class NewSystem:
    def do_new_operation(self):
        return "New System Operation"

class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def do_new_operation(self):
        return f"Adapter: {self.old_system.do_old_operation()}"

def client_code(system):
    result = system.do_new_operation()
    print(result)

old_system = OldSystem()
adapter: NewSystem = Adapter(old_system)

client_code(adapter)
