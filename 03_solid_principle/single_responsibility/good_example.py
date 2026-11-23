class EmployeeData:
  def __init__(self, name: str, department: str):
    self.name = name
    self.department = department

class PayCalculator:
  def __get_regular_hours(self):
    print("給与計算労働ロジック")
  
  def calculate_pay(self, employee_data: EmployeeData):
    self.__get_regular_hours()
    print(f"{employee_data.name}の給与を計算します。")

class HourReporter:
  def __get_regular_hours(self):
    print("労働時間計算ロジック")
  
  def report_hours(self, employee_data: EmployeeData):
    self.__get_regular_hours()
    print(f"{employee_data.name}の労働時間を報告します。")