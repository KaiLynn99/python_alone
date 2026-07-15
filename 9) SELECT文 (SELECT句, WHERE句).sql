-- ============================================
-- 1. テーブルの列情報を確認
-- ============================================
show columns from customer;


-- ============================================
-- 2. SELECT句
-- ============================================

-- 2-1. 取得する列を指定する

-- • 1つの列を取得する
select first_name
from customer
limit 10;

-- • 複数の列を取得する
select first_name, last_name
from customer
limit 10;

select last_name, first_name
from customer
limit 10;

-- • すべての列を取得する
select *
from customer
limit 10;

-- 2-2. DISTINCTによる重複の削除

-- • SELECT文の実行結果から重複する行を削除し、
--   一意の値のみを取得する
