from typing import Callable
from typing import List, Any

from PyQt5 import QtWidgets

from files.MainWindow import Ui_MainWindow
from files.ResultWindow import Ui_Form
from files.TableWindow import Ui_Form as Ui_Form_Table

from main import Calculation
from functions import change_size, get_sub
from MyThread import MyThread
from TableLoader import TableLoader
# from ChartPLTWindow import ChartPLTWindow

from settings import DEDUG

import sys


# from functions import get_super, get_sub


class Variables:
    def __init__(self, main_window):
        self.main_window: mywindow = main_window
        self.R1 = None
        self.R2 = None
        self.d = None
        self.n1 = None
        self.n2 = None
        self.n = None
        self.load()

    def load(self):
        self.R1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_8)
        self.R2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_9)
        self.d = mywindow.is_float(self.main_window.ui.doubleSpinBox_10)
        self.n1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_11)
        self.n2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_12)
        self.n = mywindow.is_float(self.main_window.ui.doubleSpinBox_13)

    def update(self):
        self.load()
        # self.main_window.table_loader1.m = self.m
        # self.main_window.table_loader2.n = self.n


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.calculation = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if DEDUG:
            self.ui.doubleSpinBox_8.setValue(10)  # R1
            self.ui.doubleSpinBox_9.setValue(5)  # R2
            self.ui.doubleSpinBox_10.setValue(3)  # d
            self.ui.doubleSpinBox_11.setValue(1)  # n1
            self.ui.doubleSpinBox_12.setValue(1)  # n2
            self.ui.doubleSpinBox_13.setValue(1.5)  # n

        change_size(self)

        self.lst_Thread = []

        self.variables = Variables(self)

        # loader1_n = 3
        # loader1_m = self.variables.m
        # loader1_label = self.ui.label_13
        # loader1_data = [
        #     ["a", 62, 350],
        #     ["b", 34, 390],
        #     ["c", 12, 120],
        #     ["d", 18, 172],
        #     ["e", 20, 200],
        #     ["f", 8, 80],
        #     ["g", 14, 120],
        # ]
        # loader1_block = False
        # loader1_heading_x = lambda iterator: \
        #     ["Наименование участков", "Количество домов на участке", "Длина участка, м"][iterator]
        # loader1_types_matrix = [[str, float, int] for _ in range(loader1_m)]

        # loader2_n = self.variables.n
        # loader2_m = 1
        # loader2_label = self.ui.label_4
        # loader2_data = [[1, 1.6]]
        # loader2_block = False
        # loader2_heading_x = lambda iterator: f"E{get_sub(str(iterator + 1))}"

        # self.table_loader1 = TableLoader(
        #     self, loader1_n, loader1_m, loader1_label,
        #     block=loader1_block,
        #     heading_x=loader1_heading_x,
        #     types_matrix=loader1_types_matrix
        # )
        # self.table_loader2 = TableLoader(
        #     self, loader2_n, loader2_m, loader2_label,
        #     block=loader2_block,
        #     heading_x=loader2_heading_x
        # )

        if DEDUG:
            pass
            # self.table_loader1.data = loader1_data
            # self.table_loader2.data = loader2_data

        # self.ui.pushButton.clicked.connect(self.table_loader1.open_table)
        # self.ui.pushButton_3.clicked.connect(self.table_loader2.open_table)

        # add_def_pushButton = lambda : self.calculation.simple_bid()
        # add_def_pushButton_2 = lambda : self.calculation.difficult_bet()
        # self.ui.pushButton.clicked.connect(lambda : self.calculate(add_def_pushButton))
        # self.ui.pushButton_2.clicked.connect(lambda : self.calculate(add_def_pushButton_2))

        add_def_pushButton = lambda: None
        self.ui.pushButton.clicked.connect(lambda: self.calculate(add_def_pushButton))

    def calculate(self, fun, *args, **kwargs):
        self.variables.update()
        # condition = self.table_loader1.valid(1, self.variables.m) and self.table_loader2.valid(
        # 1, self.variables.n)
        condition = True
        if condition:
            self.calculation = Calculation(
                R1=self.variables.R1,
                R2=self.variables.R2,
                d=self.variables.d,
                n1=self.variables.n1,
                n2=self.variables.n2,
                n=self.variables.n,
            )
            fun(*args, **kwargs)
            window = Finish(
                self
            )
            window.show()

            # def main():
            #     window.exec_()
            #
            # t = MyThread(main)
            # t.start()
            windowThread = MyThread(lambda: window.exec_())
            windowThread.start()
            self.lst_Thread.append(windowThread)

    def exec_(self) -> int:
        a = super().exec_()
        for i in self.lst_Thread:
            i.wait()
        return a

    @staticmethod
    def is_float(value: QtWidgets.QDoubleSpinBox) -> float:
        try:
            a = float(value.value())
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except ValueError:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()

    @staticmethod
    def is_int(value: QtWidgets.QDoubleSpinBox) -> int:
        try:
            a = int(round(float(value.value())))
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except ValueError:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()


class Finish(QtWidgets.QDialog):
    def __init__(self, parent: mywindow):
        super(Finish, self).__init__()
        self.ui = Ui_Form()
        self.parent = parent
        self.ui.setupUi(self)
        change_size(self)

        self.ui.doubleSpinBox_9.setValue(round(self.parent.calculation.F, 4))

        # lst = []
        # for i in range(self.parent.variables.m):
        #     data = self.parent.table_loader1.data
        #     lst.append([
        #         data[i][0], round(data[i][1], 4), round(data[i][2]),
        #         round(self.parent.calculation.lst_S[i], 3),
        #         round(self.parent.calculation.lst_S_gost[i])
        #     ])
        # print(f"{lst=}")
        #
        filter_table_results_1 = lambda dct: round(dct['value'], 3)

        loader_results_1_n = 6
        loader_results_1_m = 1
        loader_results_1_data = [[
            self.parent.calculation.OP1_F1, self.parent.calculation.H1_F1,
            self.parent.calculation.OP1_H1, self.parent.calculation.OP2_F2,
            self.parent.calculation.H2_F2, self.parent.calculation.OP2_H2,
        ]]
        types_matrix_results_1 = [[float] * loader_results_1_n]
        loader_results_1_block = True
        loader_results_1_heading_x = lambda iterator: \
            [f"ОП{get_sub('1')} - F{get_sub('1')}", f"H{get_sub('1')} - F{get_sub('1')} = f{get_sub('1')}",
             f"ОП{get_sub('1')} - H{get_sub('1')}", f"ОП{get_sub('2')} - F{get_sub('2')}",
             f"H{get_sub('2')} - F{get_sub('2')} = f{get_sub('2')}", f"ОП{get_sub('2')} - H{get_sub('2')}"][iterator]
        loader_results_1_heading_y = lambda iterator: str(iterator)
        self.table_loader_results_1 = TableLoader(
            self.parent, loader_results_1_n, loader_results_1_m, data=loader_results_1_data,
            block=loader_results_1_block,
            heading_x=loader_results_1_heading_x, heading_y=loader_results_1_heading_y,
            filter_table=filter_table_results_1, types_matrix=types_matrix_results_1
        )

        # loader_v_y_data = self.parent.calculation.lst_v_y
        # self.table_loader_v_y = TableLoader(
        #     self.parent, loader_v_d_n, loader_v_d_m, data=loader_v_y_data,
        #     block=loader_v_d_block,
        #     heading_x=loader_v_d_heading_x, heading_y=loader_v_d_heading_y,
        #     filter_table=filter_table
        # )
        #
        # loader_v_s_data = self.parent.calculation.lst_v_s
        # self.table_loader_v_s = TableLoader(
        #     self.parent, loader_v_d_n, loader_v_d_m, data=loader_v_s_data,
        #     block=loader_v_d_block,
        #     heading_x=loader_v_d_heading_x, heading_y=loader_v_d_heading_y,
        #     filter_table=filter_table
        # )

        # self.ui.doubleSpinBox_19.setValue(round(self.parent.calculation.y))
        # self.ui.doubleSpinBox_20.setValue(round(self.parent.calculation.dy))
        # self.ui.doubleSpinBox_10.setValue(round(self.parent, 2))
        self.table_loader_results_1.kwargs['block'] = True
        # self.parent.table_loader2.kwargs['block'] = True

        self.lst_Thread = []

        self.lst_Thread.append(MyThread(lambda: self.table_loader_results_1.open_table()))
        self.ui.pushButton_2.clicked.connect(
            lambda: self.lst_Thread[0].start()
        )
        #
        # self.lst_Thread.append(MyThread(lambda: self.table_loader_v_s.open_table()))
        # self.ui.pushButton_4.clicked.connect(
        #     lambda: self.lst_Thread[1].start()
        # )
        #
        # self.lst_Thread.append(MyThread(lambda: self.table_loader_v_y.open_table()))
        # self.ui.pushButton_7.clicked.connect(
        #     lambda: self.lst_Thread[2].start()
        # )
        #
        # chart_plt_w = ChartPLTWindow(1)
        # chart_plt_w.line(self.parent.calculation.chart_v_y_data)
        # chart_plt_w.quad_regress(self.parent.calculation.chart_quad_regress_data)
        #
        # self.lst_Thread.append(MyThread(
        #     lambda: chart_plt_w.start())
        # )
        # self.ui.pushButton_8.clicked.connect(
        #     lambda: self.lst_Thread[3].start()
        # )

        self.ui.pushButton.clicked.connect(self.exit_w)
        # self.ui.pushButton_2.clicked.connect(self.view_table)

    def exit_w(self):
        self.table_loader_results_1.kwargs['block'] = False
        self.close()

    # def exec_(self) -> int:
    #     a = super().exec_()
    #     for i in self.lst_Thread:
    #         i.wait()
    #     return a

    def view_table(self):
        # self.parent.table_loader1.open_table()
        # self.parent.table_loader2.open_table()
        pass


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
