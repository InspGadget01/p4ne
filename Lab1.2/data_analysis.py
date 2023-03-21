from matplotlib import pyplot
from openpyxl import load_workbook

# Загружаем таблицу Excel из файла в переменную wb
wb = load_workbook('data_analysis_lab.xlsx')
# Загружаем лист с именем Data в переменную sheet
sheet = wb['Data']


def getvalue(x):
    return x.value


# Получаем содержимое колонки A C D в виде списка
years = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))


# Создаём графическое представление
# pyplot.plot(years, label="Годы")
pyplot.plot(years, temp, label="Относит. температура")
pyplot.plot(years, activity, label="Активность")

# показываем на графике
pyplot.xlabel('Годы')
pyplot.ylabel('Активность Солнца/Температура')
pyplot.legend()
pyplot.show()
