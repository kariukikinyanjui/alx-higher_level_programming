-- List all privileges for the specified users
SELECT *
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');
