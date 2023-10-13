# SecondTask

Полностью решена поставленная задача. Заданы примеры датафреймов. Одному продукту может соответствовать несколько категорий и одной категории может соответствовать несколько продуктов.

<br>

Пример работы программы:<br>
categories_df:<br>
+----------+------------+---------+<br>
|CategoryID|CategoryName|ProductID|<br>
+----------+------------+---------+<br>
|         1|         Big|        1|<br>
|         9|       Short|        1|<br>
|         4|        Fast|        1|<br>
|         2|       Cheap|        2|<br>
|         3|       Small|        2|<br>
|        10|         New|        2|<br>
|         3|       Small|        3|<br>
|         4|        Fast|        4|<br>
|         5|        Slow|        5|<br>
|         6|        Fast|        6|<br>
|         7|   Expensive|        7|<br>
|         8|        Long|        8|<br>
|         2|       Cheap|        8|<br>
|        10|         New|        9|<br>
+----------+------------+---------+<br>

products_df:<br>
+---------+-----------+<br>
|ProductID|ProductName|<br>
+---------+-----------+<br>
|        1|        Car|<br>
|        2|      Phone|<br>
|        3|      House|<br>
|        4|         PC|<br>
|        5|     Laptop|<br>
|        6|     Tablet|<br>
|        7|      Grain|<br>
|        8|   Concrete|<br>
|        9|   Software|<br>
|       10|   Hardware|<br>
|       11|     Trucks|<br>
+---------+-----------+<br>

<br>

result_df:<br>
+-----------+------------+<br>
|ProductName|CategoryName|<br>
+-----------+------------+<br>
|        Car|        Fast|<br>
|        Car|       Short|<br>
|        Car|         Big|<br>
|      Phone|         New|<br>
|      Phone|       Small|<br>
|      Phone|       Cheap|<br>
|      House|       Small|<br>
|         PC|        Fast|<br>
|     Laptop|        Slow|<br>
|     Tablet|        Fast|<br>
|      Grain|   Expensive|<br>
|   Concrete|       Cheap|<br>
|   Concrete|        Long|<br>
|   Software|         New|<br>
|   Hardware|        NULL|<br>
|     Trucks|        NULL|<br>
+-----------+------------+<br>

<br>

продукты, у которых нет категорий имеют NULL в столбце CategoryName.