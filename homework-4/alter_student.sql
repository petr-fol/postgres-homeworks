-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
    student_id SERIAL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthday DATE,
    phone VARCHAR(32)
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER  TABLE student ADD COLUMN middle_name VARCHAR(50);

-- 3. Удалить колонку middle_name
DROP COLUMN  middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER COLUMN birthday RENAME TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER  COLUMN phone TYPE VARCHAR(32);

-- 6. Вставить три любых записи с авто-генерацией идентификатора
INSERT INTO student (first_name, last_name, birthday, phone)
VALUES
    ('Иван', 'Иванов', '2000-01-01', '123-456-7890'),
    ('Мария', 'Петрова', '1998-05-15', '987-654-3210'),
    ('Алексей', 'Сидоров', '2002-08-20', '555-123-4567');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;