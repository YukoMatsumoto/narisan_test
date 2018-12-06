--customers テーブルがあったら削除する
DROP TABLE IF EXISTS customers;


-- customers テーブルをつくる

CREATE TABLE customers (
    name TEXT
);


-- 初期データをいくつかいれる
INSERT INTO
    customers
VALUES
('Bob'
;