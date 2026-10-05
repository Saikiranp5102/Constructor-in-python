# Example-1

# class Bank:
#     bank_name = "Bank of India"
#     branch_name = "Vizianagaram"
#     def __init__(self, cust_name, acc_no, acc_type, acc_bal):
#         self.customer_name = cust_name
#         self.account_number = acc_no
#         self.account_type = acc_type
#         self.account_balance = acc_bal
#     def displayDetails(self):
#         print("Bank Name : ",Bank.bank_name)
#         print("Branch Location : ",Bank.branch_name)
#         print("Account holder Name : ", self.customer_name)
#         print("Account Number : ", self.account_number)
#         print("Account Type : ", self.account_type)
#         print("Account balance : ", self.account_balance)
# cust1 = Bank("Rajeev", 15676778, "Savings Account", 627289)
# cust2 = Bank("Nani", 15789992, "Current Account", 72127192)
# cust3 = Bank("Gagan", 16778181, "Savings Account", 27718)
# print("===========Customer-1 details=============")
# cust1.displayDetails()
# print("===========Customer-2 details=============")
# cust2.displayDetails()
# print("===========Customer-3 details=============")
# cust3.displayDetails()



# Example-2

# class School:
#     school_name = "LittleJoys"
#     school_location = "Visakhapatnam"
#     def __init__(self,std_name, std_age, std_add, std_gender):
#         self.student_name = std_name
#         self.student_age = std_age
#         self.student_address = std_add
#         self.student_gender = std_gender
#     def displayDetails(self):
#         print("School Name : ", School.school_name)
#         print("School Location : ", School.school_location)
#         print("Student Name : ", self.student_name)
#         print("Student Age : ", self.student_age)
#         print("Student Address : ", self.student_address)
#         print("Student gender : ", self.student_gender)
# std1 = School("Nithin", 5, "Gajuwaka", "Male")
# std2 = School("Bharath", 7, "Dwarakanagar", "Male")
# std3 = School("Sravanthi", 9, "Gopalapatnam", "Female")
# print("===========Student-1 details=============")
# std1.displayDetails()
# print("===========Student-2 details=============")
# std2.displayDetails()
# print("===========Student-3 details=============")
# std3.displayDetails()




# Example-3

class Train_Reservation:
    Train_Name = "Godavari SF Express"
    Train_Number = 12727
    Boarding = "Secundrabad"
    Destination = "Visakhapatnam"
    def __init__(self, pass_name, pass_age, pnr_no, altd_berth):
        self.Passenger_name = pass_name
        self.Passenger_age = pass_age
        self.PNR_number = pnr_no
        self.Allotted_berth = altd_berth
    def displayDetails(self):
        print("Train Name : ", Train_Reservation.Train_Name)
        print("Train Number : ", Train_Reservation.Train_Number)
        print("Boarding Station : ", Train_Reservation.Boarding)
        print("Destination : ", Train_Reservation.Destination)
        print("Passenger Name : ", self.Passenger_name)
        print("Passenger age : ", self.Passenger_age)
        print("PNR Number : ", self.PNR_number)
        print("Allotted berth : ", self.Allotted_berth)
psgr1 = Train_Reservation("Raghu", 50, 4567677888, "S1 63 L")
psgr2 = Train_Reservation("Lakshmi", 65, 4573892278, "B2 13 L")
psgr3 = Train_Reservation("Yatheen", 25, 4820171362, "S8 74 SU")
print("===========Passenger-1 details=============")
psgr1.displayDetails()
print("===========Passenger-2 details=============")
psgr2.displayDetails()
print("===========Passenger-3 details=============")
psgr3.displayDetails()


