class XlxsDada:
    def __init__(self, parser):
        self.parser = parser

    def z_report(self):
        return self.parser.by_name(self.parser.Z_REPORT)

    def bar_income(self):
        return self.parser.by_name(self.parser.BAR_INCOME)

    def add_income_mess(self):
        return None

    def admin_income(self):
        return self.parser.by_name(self.parser.ADMIN_INCOME)

    def change_money(self):
        return self.parser.by_name(self.parser.CHANGE_MONEY)

    def total_income(self):
        return self.parser.by_name(self.parser.TOTAL_INCOME)

    def expenses_mess(self):
        lst = []
        for name, v in self.parser.expense()["expense"]:
            lst.append("- {} - {} грн.<br>".format(name, v))
        return "".join(lst)

    def change_money_expenses(self):
        return self.parser.by_name(self.parser.CHANGE_MONEY_EXPENSES)

    def salary_mess(self):
        lst = []
        for name, v in self.parser.expense()["salary"]:
            lst.append("- {} - {} грн.<br>".format(name, v))
        return "".join(lst)

    def all_expenses(self):
        return self.parser.by_name(self.parser.ALL_EXPENSES)

    def total_in_safe(self):
        return self.parser.by_name(self.parser.TOTAL_IN_SAFE)
