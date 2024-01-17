SELECT w.name, w.population, w.area
FROM World AS w
WHERE w.area >= 3.E6
OR w.population >= 2.5E7;