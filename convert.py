from decimal_to import decimal

solution=decimal()

class Number_system:
    def solv(self,number,base1,base2):
        real_number=solution.str_to_Number(number,base1)
        result=solution.decimal_to_base(real_number,base2)
        return result
        