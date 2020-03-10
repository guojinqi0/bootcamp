--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT 
	e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM 
	employees e INNER JOIN salaries s ON e.emp_no = s.emp_no;

--2. List employees who were hired in 1986.
SELECT 
	first_name, last_name, hire_date 
FROM 
	employees 
WHERE hire_date BETWEEN '01/01/1986' AND '12/31/1986';

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
WITH department_name_manager AS
	(SELECT
	 	d.dept_no, dept_name, emp_no, from_date, to_date

	 FROM
	 	departments d JOIN dept_manager dm ON d.dept_no = dm.dept_no)
SELECT 
	dnm.dept_no, dnm.dept_name, e.emp_no, e.last_name, e.first_name, dnm.from_date, dnm.to_date
FROM 
	department_name_manager dnm JOIN employees e ON dnm.emp_no = e.emp_no;


--4. List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT 
	de.emp_no, e.last_name, e.first_name, d.dept_name
FROM 
	dept_emp de
	JOIN employees e ON de.emp_no = e.emp_no
	JOIN departments d ON de.dept_no = d.dept_no;

--5. List all employees whose first name is "Hercules" and last names begin with "B".
SELECT 
	first_name, last_name
FROM 
	employees 
WHERE 
	first_name ILIKE 'Hercules' AND last_name ILIKE 'B%';

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT 
	de.emp_no, e.last_name, e.first_name, d.dept_name
FROM 
	dept_emp de JOIN employees e ON de.emp_no = e.emp_no
	JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name ILIKE 'Sales';

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT 
	de.emp_no, e.last_name, e.first_name, d.dept_name
FROM 
	dept_emp de
	JOIN employees e ON de.emp_no = e.emp_no
	JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name IN ('Sales', 'Development');

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT 
	last_name, COUNT(last_name) AS frequency
FROM 
	employees
GROUP BY last_name
ORDER BY frequency DESC;