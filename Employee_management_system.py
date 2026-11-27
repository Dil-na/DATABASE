# import csv
import sqlite3

DATABASE = "company.db"
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS employees (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		email TEXT UNIQUE NOT NULL,
		department TEXT NOT NULL,
		salary REAL NOT NULL CHECK (salary > 0),
		join_date TEXT NOT NULL DEFAULT CURRENT_DATE,
		is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
	)
""")
conn.commit()

DISPLAY_COLUMNS = "id, name, email, department, salary, join_date"


def _show_rows(rows):
	if not rows:
		print("No employees found.")
		return
	print("ID | Name | Email | Department | Salary | Join date")
	for row in rows:
		print(" | ".join(str(value) for value in row))


def add_employee(name, email, department, salary):
	try:
		salary = float(salary)
	except (TypeError, ValueError):
		print("Please enter a valid salary greater than 0.")
		return
	if salary <= 0:
		print("Salary must be greater than 0.")
		return
	if not isinstance(email, str) or "@" not in email:
		print("Please enter a valid email address containing @.")
		return
	if not name or not department:
		print("Name and department are required.")
		return
	try:
		cursor.execute(
			"INSERT INTO employees (name, email, department, salary) VALUES (?, ?, ?, ?)",
			(name, email, department, salary),
		)
		conn.commit()
		print("Employee added successfully.")
	except sqlite3.IntegrityError as error:
		conn.rollback()
		if "employees.email" in str(error):
			print("An employee with that email already exists.")
		else:
			print("Could not add employee. Please check the employee details.")


def view_employees():
	cursor.execute("SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? ORDER BY id", (1,))
	_show_rows(cursor.fetchall())


def get_employee(employee_id):
	cursor.execute("SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE id = ?", (employee_id,))
	row = cursor.fetchone()
	if row is None:
		print("Not found.")
	else:
		_show_rows([row])


def search_employee(keyword):
	cursor.execute(
		"SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? AND LOWER(name) LIKE LOWER(?) ORDER BY id",
		(1, "%" + str(keyword) + "%"),
	)
	_show_rows(cursor.fetchall())


def filter_by_department(dept):
	cursor.execute(
		"SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? AND LOWER(department) = LOWER(?) ORDER BY id",
		(1, dept),
	)
	_show_rows(cursor.fetchall())


def filter_by_salary(min_salary, max_salary):
	try:
		min_salary, max_salary = float(min_salary), float(max_salary)
	except (TypeError, ValueError):
		print("Please enter valid salary amounts.")
		return
	if min_salary > max_salary:
		print("Minimum salary cannot exceed maximum salary.")
		return
	cursor.execute(
		"SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? AND salary BETWEEN ? AND ? ORDER BY salary",
		(1, min_salary, max_salary),
	)
	_show_rows(cursor.fetchall())


def sort_employees(column, order):
	columns = {"name": "name", "salary": "salary", "join_date": "join_date"}
	column, order = str(column).lower(), str(order).upper()
	if column not in columns or order not in ("ASC", "DESC"):
		print("Sort by name, salary, or join_date; order must be ASC or DESC.")
		return
	cursor.execute(
		"SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? ORDER BY " + columns[column] + " " + order,
		(1,),
	)
	_show_rows(cursor.fetchall())


def _update(employee_id, column, value):
	if column == "salary":
		try:
			value = float(value)
		except (TypeError, ValueError):
			print("Please enter a valid salary greater than 0.")
			return
		if value <= 0:
			print("Salary must be greater than 0.")
			return
	if column == "department" and not value:
		print("Department is required.")
		return
	cursor.execute("UPDATE employees SET " + column + " = ? WHERE id = ?", (value, employee_id))
	if cursor.rowcount == 0:
		print("No employee found.")
		return
	conn.commit()
	print("Employee updated successfully.")


def update_salary(employee_id, new_salary):
	_update(employee_id, "salary", new_salary)


def update_department(employee_id, new_dept):
	_update(employee_id, "department", new_dept)


def give_raise(department, percent):
	try:
		percent = float(percent)
	except (TypeError, ValueError):
		print("Please enter a valid percentage.")
		return
	cursor.execute(
		"UPDATE employees SET salary = salary * ? WHERE is_active = ? AND LOWER(department) = LOWER(?)",
		(1 + percent / 100, 1, department),
	)
	updated = cursor.rowcount
	conn.commit()
	print(str(updated) + " employees updated.")


def remove_employee(employee_id):
	cursor.execute("SELECT id FROM employees WHERE id = ? AND is_active = ?", (employee_id, 1))
	if cursor.fetchone() is None:
		print("No employee found.")
		return
	if input("Remove this employee? (y/n): ").strip().lower() != "y":
		print("Removal cancelled.")
		return
	cursor.execute("UPDATE employees SET is_active = ? WHERE id = ?", (0, employee_id))
	conn.commit()
	print("Employee removed.")


def restore_employee(employee_id):
	cursor.execute("UPDATE employees SET is_active = ? WHERE id = ? AND is_active = ?", (1, employee_id, 0))
	if cursor.rowcount == 0:
		print("No employee found.")
		return
	conn.commit()
	print("Employee restored.")


def view_removed():
	cursor.execute("SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? ORDER BY id", (0,))
	_show_rows(cursor.fetchall())


def show_summary():
	cursor.execute(
		"SELECT COUNT(*), AVG(salary), MAX(salary), MIN(salary) FROM employees WHERE is_active = ?",
		(1,),
	)
	total, average, highest, lowest = cursor.fetchone()
	print("Total active employees: " + str(total))
	print("Average salary: " + str(average))
	print("Highest salary: " + str(highest))
	print("Lowest salary: " + str(lowest))
	print("Employees and average salary by department:")
	cursor.execute(
		"SELECT department, COUNT(*), AVG(salary) FROM employees WHERE is_active = ? GROUP BY department ORDER BY department",
		(1,),
	)
	for department, count, dept_average in cursor.fetchall():
		print(str(department) + ": " + str(count) + " employees, average salary " + str(dept_average))


def top_earners(n):
	try:
		n = int(n)
	except (TypeError, ValueError):
		print("Please enter a valid number.")
		return
	if n < 0:
		print("The number must not be negative.")
		return
	cursor.execute(
		"SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? ORDER BY salary DESC LIMIT ?",
		(1, n),
	)
	_show_rows(cursor.fetchall())


# def export_to_csv(filename):
# 	try:
# 		cursor.execute("SELECT " + DISPLAY_COLUMNS + " FROM employees WHERE is_active = ? ORDER BY id", (1,))
# 		with open(filename, "w", newline="", encoding="utf-8") as csv_file:
# 			writer = csv.writer(csv_file)
# 			writer.writerow(("id", "name", "email", "department", "salary", "join_date"))
# 			writer.writerows(cursor.fetchall())
# 		print("Employees exported successfully.")
# 	except (OSError, TypeError) as error:
# 		print("Could not export employees: " + str(error))


def _number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")


def main():
	while True:
		print("\n1 Add  2 View  3 Search  4 Filter department  5 Filter salary  6 Sort")
		print("7 Update salary  8 Give raise  9 Remove  10 Restore  11 Summary")
		print("12 Top earners  13 Export CSV  14 Exit  15 Get employee")
		print("16 Update department  17 View removed")
		choice = input("Choose an option: ").strip()
		if choice == "14":
			return
		try:
			if choice == "1":
				add_employee(input("Name: "), input("Email: "), input("Department: "), _number("Salary: "))
			elif choice == "2":
				view_employees()
			elif choice == "3":
				search_employee(input("Name keyword: "))
			elif choice == "4":
				filter_by_department(input("Department: "))
			elif choice == "5":
				filter_by_salary(_number("Minimum salary: "), _number("Maximum salary: "))
			elif choice == "6":
				sort_employees(input("Column: "), input("Order (ASC/DESC): "))
			elif choice == "7":
				update_salary(input("Employee id: "), _number("New salary: "))
			elif choice == "8":
				give_raise(input("Department: "), _number("Raise percentage: "))
			elif choice == "9":
				remove_employee(input("Employee id: "))
			elif choice == "10":
				restore_employee(input("Employee id: "))
			elif choice == "11":
				show_summary()
			elif choice == "12":
				top_earners(input("Number of employees: "))
			# elif choice == "13":
			# 	export_to_csv(input("CSV filename: "))
			elif choice == "15":
				get_employee(input("Employee id: "))
			elif choice == "16":
				update_department(input("Employee id: "), input("New department: "))
			elif choice == "17":
				view_removed()
			else:
				print("Please choose a valid menu option.")
		except sqlite3.Error as error:
			conn.rollback()
			print("Could not complete the operation: " + str(error))


if __name__ == "__main__":
	try:
		main()
	finally:
		conn.commit()
		conn.close()
