class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, full_name, phone, email, position, office, skype):
        self.employees[full_name] = {
            "Телефон": phone,
            "Email": email,
            "Посада": position,
            "Кабінет": office,
            "Skype": skype
        }
        print(f'Працівник {full_name} доданий.')

    def remove_employee(self, full_name):
        if full_name in self.employees:
            del self.employees[full_name]
            print(f'Працівник {full_name} видалений.')
        else:
            print(f'Працівник {full_name} не знайдений.')

    def find_employee(self, full_name):
        return self.employees.get(full_name, f'Працівник {full_name} не знайдений.')

    def update_employee(self, full_name, field, new_value):
        if full_name in self.employees:
            if field in self.employees[full_name]:
                self.employees[full_name][field] = new_value
                print(f'Оновлено {field} для {full_name}.')
            else:
                print(f'Поле "{field}" не знайдено.')
        else:
            print(f'Працівник {full_name} не знайдений.')

    def show_all(self):
        if self.employees:
            print("\nСписок працівників:")
            for name, data in self.employees.items():
                print(f'{name}: {data}')
        else:
            print("Список працівників порожній.")

company = Company()

company.add_employee("Іван Петренко", "+380671234567", "ivan.petrenko@company.com", "Менеджер", "101", "ivan.petrenko")
company.add_employee("Олена Сидорова", "+380931234567", "olena.sydorova@company.com", "Бухгалтер", "202", "olena.sydorova")

print(company.find_employee("Іван Петренко"))

company.update_employee("Олена Сидорова", "Кабінет", "203")

company.remove_employee("Іван Петренко")

company.show_all()