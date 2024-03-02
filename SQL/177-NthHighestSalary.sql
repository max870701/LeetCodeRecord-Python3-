CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT
        SalaryRank.salary
    FROM (
        SELECT
            e.salary,
            DENSE_RANK() OVER(ORDER BY e.salary DESC) AS rank
        FROM Employee AS e
    ) AS SalaryRank
    WHERE SalaryRank.rank = N
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;