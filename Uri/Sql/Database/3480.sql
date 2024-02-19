CREATE TABLE chairs (
    id numeric PRIMARY KEY,
    queue numeric,
    available boolean
);

INSERT INTO chairs (id, queue, available) VALUES
(1, 1, FALSE),
(2, 1, FALSE),
(3, 1, TRUE),
(4, 1, FALSE),
(5, 1, FALSE),
(6, 1, FALSE),
(7, 1, TRUE),
(8, 1, TRUE),
(9, 2, TRUE),
(10, 2, FALSE),
(11, 2, TRUE),
(12, 2, TRUE),
(13, 2, FALSE),
(14, 2, TRUE),
(15, 2, TRUE),
(16, 2, FALSE),
(17, 3, TRUE),
(18, 3, FALSE),
(19, 3, TRUE),
(20, 3, FALSE),
(21, 3, TRUE),
(22, 3, TRUE),
(23, 3, FALSE),
(24, 3, FALSE),
(25, 4, TRUE),
(26, 4, FALSE),
(27, 4, FALSE),
(28, 4, TRUE),
(29, 4, TRUE),
(30, 4, FALSE),
(31, 4, FALSE),
(32, 4, TRUE);

-- DROP TABLE chairs