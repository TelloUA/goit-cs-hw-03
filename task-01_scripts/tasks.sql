SELECT * FROM tasks WHERE user_id = 3;

SELECT tasks.*, status.name FROM tasks
INNER JOIN status on status.id = tasks.status_id
WHERE status.name = 'new';

UPDATE tasks SET status_id = 2 WHERE id = 15; 

SELECT *
FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks
);

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Buy tomatoes', 'Need to buy tasty tomatoes in shop', 2, 4); 

SELECT tasks.*, status.name FROM tasks
INNER JOIN status on status.id = tasks.status_id
WHERE status.name != 'completed';

DELETE FROM tasks WHERE id = 10;

SELECT * FROM users WHERE email LIKE '%example%';

UPDATE users SET fullname = 'Andrew Johnson' WHERE id = 1;

SELECT COUNT(tasks.id), status.name FROM tasks
INNER JOIN status ON status.id = tasks.status_id
GROUP BY status.name;

SELECT tasks.*, users.email
FROM tasks 
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

SELECT * FROM tasks
WHERE description IS NULL OR description = '';

SELECT users.*, tasks.*
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

SELECT users.id AS users_id, fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname
ORDER BY task_count DESC;
