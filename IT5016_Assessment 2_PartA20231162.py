class RequisitionSystem:
    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.approval_ref_number = "Not available" 
        self.total = 0 

    def staff_info(self,staff_id,staff_name,requisition_id):
        date = input("Enter the date: ")
        staff_id = input("Enter the staff ID: ")
        staff_name = input("Enter the staff name: ")
        counter = 1
        requisition_id = 10000+counter
        print("Printing staff information")
        print("Date: ", date)
        print("Staff id: ", staff_id)
        print("Staff_name: ", staff_name)
        print("Requisition id: ", requisition_id)
        return date, staff_id, staff_name, requisition_id
   



    def requisitions_details(self,total):
        staff_info()
        total = 0
        num_items = int(input("\nHow many requisition items do you have? "))
        for i in range(num_items):
            item_name = input(f"Enter the name of item {i+1}: ")
            item_price = int(input(f"Enter the price of {item_name}: $"))
            total += item_price
        print(f"\nTotal requisition value: ${total:.2f}")
        return total
    requisitions_details()


    def requisitions_approval(self,status):
        total= requisitions_total()
        status = "Pending"
        approval_ref_number = None
    
        
        if total < 500:
            status = "Approved"
            approval_ref_number = f"{staff_id}{str(requisition_id)[-3:]}"
        
        print("Total: $" , total) 
        print("Status: " , status)
        
        if approval_ref_number:
            print(f"Approval Reference Number: {approval_ref_number}")
        return total,status,approval_ref_number
    requisitions_approval()

    def display_requisitons(self):
        date,requisition_id,staff_id,staff_name=staff_info()
        total,status,approval_ref_number=requisitions_approval()
        
        
        print("Printing Requisitions:")
        print("Date: ",self.date)
        print("Requisition ID: ",self.requisition_id)
        print("Staff ID: ",self.staff_id)
        print("Staff Name: ",self.staff_name)
        print("Total: $",self.total)
        print("Status: ",self.status)
        print("approval reference no:",self.approval_ref_number)
        
        
    display_requisitons()
RequisitionSystem()