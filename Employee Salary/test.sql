SELECT 
    department, 
    ROUND(AVG(salary)) AS avg_salary
FROM employee
GROUP BY department
ORDER BY department ASC;