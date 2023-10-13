# SecondTask

Полностью решена поставленная задача. Заданы примеры датафреймов. Одному продукту может соответствовать несколько категорий и одной категории может соответствовать несколько продуктов.

Пример работы программы:
categories_df:
+----------+------------+---------+
|CategoryID|CategoryName|ProductID|
+----------+------------+---------+
|         1|         Big|        1|
|         9|       Short|        1|
|         4|        Fast|        1|
|         2|       Cheap|        2|
|         3|       Small|        2|
|        10|         New|        2|
|         3|       Small|        3|
|         4|        Fast|        4|
|         5|        Slow|        5|
|         6|        Fast|        6|
|         7|   Expensive|        7|
|         8|        Long|        8|
|         2|       Cheap|        8|
|        10|         New|        9|
+----------+------------+---------+

products_df:
+---------+-----------+
|ProductID|ProductName|
+---------+-----------+
|        1|        Car|
|        2|      Phone|
|        3|      House|
|        4|         PC|
|        5|     Laptop|
|        6|     Tablet|
|        7|      Grain|
|        8|   Concrete|
|        9|   Software|
|       10|   Hardware|
|       11|     Trucks|
+---------+-----------+

result_df:
+-----------+------------+
|ProductName|CategoryName|
+-----------+------------+
|        Car|        Fast|
|        Car|       Short|
|        Car|         Big|
|      Phone|         New|
|      Phone|       Small|
|      Phone|       Cheap|
|      House|       Small|
|         PC|        Fast|
|     Laptop|        Slow|
|     Tablet|        Fast|
|      Grain|   Expensive|
|   Concrete|       Cheap|
|   Concrete|        Long|
|   Software|         New|
|   Hardware|        NULL|
|     Trucks|        NULL|
+-----------+------------+

продукты, у которых нет категорий имеют NULL в столбце CategoryName.