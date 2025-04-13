class RequisitionSystem:      #start class by the name Requisition system 
    def __init__(self):
        self.requisition_id= 10000
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.approval_ref_number = "Not available"
        self.total = 0
        self.requisition_id = 0
        self.status = "Pending"

    def staff_info(self):        #asking user for their personal details
        self.requisition_id= 10000
        self.date = input("Enter the date: ")
        self.staff_id = input("Enter the staff ID: ")
        self.staff_name = input("Enter the staff name: ")
        self.requisition_id += 1
        print("Printing staff information:")      #outcome of the ppersonal detail come from here
        print("Date: ", self.date)
        print("Staff ID: ", self.staff_id)
        print("Staff Name: ", self.staff_name)
        print("Requisition ID: ", self.requisition_id)

    def requisitions_details(self):
        self.staff_info()
        self.total = 0
        num_items = int(input("\nHow many requisition items do you have? "))
        for i in range(num_items):                  #asking user for their items and price
            item_name = input(f"Enter the name of item {i+1}: ")
            item_price = float(input(f"Enter the price of {item_name}: $"))
            self.total += item_price
        print(f"\nTotal requisition value: ${self.total:.2f}")

    def requisitions_approval(self):
        if self.total < 500:
            self.status = "Approved"                  #here we will define its approved or not
            self.approval_ref_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        print("Total: $", self.total)
        print("Status: ", self.status)
        if self.approval_ref_number != "Not available":
            print(f"Approval Reference Number: {self.approval_ref_number}")

    def display_requisitions(self):
        self.requisitions_details()
        self.requisitions_approval()
        print("Printing Requisitions:")
        print("Date: ", self.date)
        print("Requisition ID: ", self.requisition_id)
        print("Staff ID: ", self.staff_id)
        print("Staff Name: ", self.staff_name)
        print("Total: $", self.total)
        print("Status: ", self.status)
        print("Approval Reference No: ", self.approval_ref_number)

requisition_system = RequisitionSystem()
requisition_system.display_requisitions()
