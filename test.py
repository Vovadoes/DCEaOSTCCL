# lst = []
#
# a = input()
# while a != '1':
#     lst.append(a)
#     a = input()
#
# for i in lst:
#     a, b = i.split('=')
#     print(f"{a} = self.variables.{a},")


# self.da_np = mywindow.is_float(self.main_window.ui.doubleSpinBox_31)

def f1(s):
    lst1 = []
    lst2 = []
    lst4 = []

    lst = s.split(', ')

    for i in lst:
        lst1.append(f"{i}=self.variables.{i},")
        lst2.append(f"self.{i} = mywindow.is_float(self.main_window.ui.doubleSpinBox)")
        lst4.append(f"self.{i}=None")

    print()
    for i in lst4:
        print(i)
    print()
    for i in lst2:
        print(i)
    print()
    for i in lst1:
        print(i)


s = 'R1, R2, d, n1, n2, n'
f1(s)
#
lst = '''self.R1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_8)
        self.R2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_9)
        self.d = mywindow.is_float(self.main_window.ui.doubleSpinBox_10)
        self.n1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_11)
        self.n2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_12)
        self.n = mywindow.is_float(self.main_window.ui.doubleSpinBox_13)'''\
    .replace('        ', '').replace('(', ')').split('\n')

for i in lst:
    a = i.split(')')
    print(f"self.ui.{a[1].split('.')[3]}.setValue()  # {a[0].split('=')[0].split('.')[1]}")
