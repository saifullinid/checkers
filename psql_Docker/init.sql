CREATE USER checkers_su SUPERUSER PASSWORD '123456';
CREATE DATABASE checkers OWNER checkers_su;
GRANT ALL PRIVILEGES ON DATABASE checkers TO checkers_su;