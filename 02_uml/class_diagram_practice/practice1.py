class Employee:
    __emp_id: int
    __name: str
    __salary: int


    def __init__(self, emp_id: int, name: str, salary: int):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # def _work(self)-> None:
    #     print(f"{self.__name} は働きます。")

    # def get_salary(self) -> int:
    #     return self.__salary

    # def set_salary(self, salary: int) -> None:
    #     self.__salary = salary
    
    @property
    def salary(self) -> int:
        return self.__salary


