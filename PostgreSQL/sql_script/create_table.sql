-- 创建用户表
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    created TIMESTAMP);

-- 创建项目表
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    created TIMESTAMP,
    created_by_user_id INT REFERENCES users(user_id));
