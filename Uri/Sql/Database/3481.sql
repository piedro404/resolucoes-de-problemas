CREATE TABLE nodes (
    node_id numeric,
    pointer numeric
);

insert into nodes (node_id, pointer) values
(50, 30),
(50, 75),
(30, 15),
(30, 35),
(15, 1),
(15, 20),
(35, 32),
(35, 40),
(1, null),
(20, null),
(32, null),
(40, null),
(75, 60),
(75, 90),
(60, 55),
(60, 70),
(90, 80),
(90, 95),
(55, null),
(70, null),
(80, null),
(95, null);

/*  Execute this query to drop the tables */
-- DROP TABLE nodes;