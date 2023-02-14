-- Import in hbtn_0c_0 database a table dump
-- display average temperature (Fahrn) by city ordered by temperature (desc)
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
