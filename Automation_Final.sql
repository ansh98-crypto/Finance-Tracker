
--Check if table already exists, if yes then delete existing
--if OBJECT_ID('update_loan') is not null drop procedure update_loan
--GO
--IF OBJECT_ID('Loan2') IS NOT NULL Drop TABLE Loan2
--Create Database Personal_Finance_ 

--Drop Procedure data_updation

---IF OBJECT_ID('data_updation') is NOT NULL

create or alter procedure data_updation as
begin
IF OBJECT_ID('PF_DATA') IS NOT NULL Drop TABLE PF_DATA
--https://stackoverflow.com/questions/45217560/how-use-bulk-insert-csv-to-sql-server-with-datetime-format-correct
SET DATEFORMAT DMY;
Create Table PF_DATA
(
[Date] DateTime Null,
[Narration] NVarChar(500) Null,
[Withdrawal Amt] Float Null,
[Deposit Amt] Float Null,
[Unique] NVarchar(500) Null,
[Expense Vendor] char(500) Null,
[Expense Classification] Char(500) Null,
[Expense Details] Char(500) Null,
[Inflow Classification] Char(500) Null,

)


Bulk Insert PF_DATA
From 'C:\Users\ansht\Desktop\Projects\Analytics\Git Hub\Personal Finance - Git\Cleaned_CSV.csv'
With (Format = 'CSV', FirstRow=2)
--Step 2: Import the Data
Select * from PF_DATA

end;


--CREATE PROCEDURE wrapper as
