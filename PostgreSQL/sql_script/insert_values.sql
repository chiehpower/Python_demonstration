-- 插入数据
-- 插入用户数据
INSERT INTO users (username, created)
VALUES ('user1', NOW());

-- 插入更多用户数据
INSERT INTO users (username, created)
VALUES ('user2', '2023-10-25 14:45:00');

-- 插入项目数据，将项目关联到特定用户
INSERT INTO projects (project_name, created, created_by_user_id)
VALUES ('Project A', '2023-10-30 14:45:00', 1); -- 项目A由user1创建

-- 插入更多项目数据
INSERT INTO projects (project_name, created, created_by_user_id)
VALUES ('Project B', '2023-10-31 14:45:00', 2); -- 项目B由user2创建
