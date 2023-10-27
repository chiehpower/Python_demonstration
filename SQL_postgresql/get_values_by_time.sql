SELECT * FROM users
WHERE created >= '2023-10-26 00:00:00' AND created <= '2023-10-27 05:00:00';

SELECT * FROM projects
WHERE created >= '2023-10-30 00:00:00' AND created <= '2023-10-31 00:00:00';

SELECT users.username, projects.project_name
FROM users
JOIN projects ON users.user_id = projects.created_by_user_id
WHERE projects.created >= '2023-10-30 00:00:00' AND projects.created <= '2023-10-31 00:00:00'
AND projects.project_name = 'Project A';

SELECT projects.project_name
FROM projects
WHERE projects.created >= '2023-10-30 00:00:00' AND projects.created <= '2023-10-31 00:00:00'
AND projects.project_name = 'Project A';

SELECT u.username, p.project_name
FROM projects p
JOIN users u ON p.created_by_user_id = u.user_id
WHERE p.created >= '2023-10-30 00:00:00' AND p.created <= '2023-10-31 00:00:00'
AND p.project_name = 'Project A'
AND u.username = 'user1';
