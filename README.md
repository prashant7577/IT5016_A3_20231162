# Requisition System – Python Program

This program is a basic **Requisition Management System** written in Python.  
It allows a staff member to submit a requisition request, calculates the total cost of requested items, and determines if the request is approved based on a set limit.

---

## Features

- Collects **staff details** (date, ID, and name).
- Takes multiple **requisition items** with prices.
- Calculates the **total cost** of the requisition.
- Approves the requisition if the total is **less than $500**.
- Generates an **approval reference number** if approved.
- Displays all entered and processed information.

---

## How It Works

### 1. Staff Info Input
- User is asked to enter the **date**, **staff ID**, and **staff name**.
- Requisition ID starts at `10000` and increases by 1.

### 2. Requisition Items
- User inputs the number of items.
- For each item:
  - Enter the **name** and **price**.
- The system calculates and displays the **total cost**.

### 3. Approval Check
- If total is **below $500**:
  - Status becomes **"Approved"**.
  - An **approval reference number** is created using staff ID and requisition ID.
- If total is **$500 or more**:
  - Status remains **"Pending"**.
  - No reference number is generated.

### 4. Display Section
- Final requisition details are printed, including:
  - Date
  - Requisition ID
  - Staff ID
  - Staff Name
  - Total
  - Status
  - Approval Reference Number (if applicable)

---


