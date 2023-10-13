from pyspark import Row
from pyspark.sql import SparkSession


def get_products_with_categories(products_df, categories_df):
    # Выполним left-outer join между продуктами
    # и категориями в общем столбце, используя идентификатор продукта
    result_df = products_df.join(categories_df, 'ProductID', 'left_outer')

    # Выберем необходимые колонки
    result_df = result_df.select('ProductName', 'CategoryName')

    return result_df


if __name__ == '__main__':
    spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

    # набор продуктов
    products_data = [
        Row(ProductID=1, ProductName="Car"),
        Row(ProductID=2, ProductName="Phone"),
        Row(ProductID=3, ProductName="House"),
        Row(ProductID=4, ProductName="PC"),
        Row(ProductID=5, ProductName="Laptop"),
        Row(ProductID=6, ProductName="Tablet"),
        Row(ProductID=7, ProductName="Grain"),
        Row(ProductID=8, ProductName="Concrete"),
        Row(ProductID=9, ProductName="Software"),
        Row(ProductID=10, ProductName="Hardware"),
        Row(ProductID=11, ProductName="Trucks")
    ]

    # набор категорий
    categories_data = [
        Row(CategoryID=1, CategoryName="Big", ProductID=1),
        Row(CategoryID=9, CategoryName="Short", ProductID=1),
        Row(CategoryID=4, CategoryName="Fast", ProductID=1),
        Row(CategoryID=2, CategoryName="Cheap", ProductID=2),
        Row(CategoryID=3, CategoryName="Small", ProductID=2),
        Row(CategoryID=10, CategoryName="New", ProductID=2),
        Row(CategoryID=3, CategoryName="Small", ProductID=3),
        Row(CategoryID=4, CategoryName="Fast", ProductID=4),
        Row(CategoryID=5, CategoryName="Slow", ProductID=5),
        Row(CategoryID=6, CategoryName="Fast", ProductID=6),
        Row(CategoryID=7, CategoryName="Expensive", ProductID=7),
        Row(CategoryID=8, CategoryName="Long", ProductID=8),
        Row(CategoryID=2, CategoryName="Cheap", ProductID=8),
        Row(CategoryID=10, CategoryName="New", ProductID=9)
    ]

    # датафрейм для категорий
    categories_df = spark.createDataFrame(categories_data)

    print('categories_df:')
    categories_df.show()

    # датафрейм для продуктов
    products_df = spark.createDataFrame(products_data)

    print('products_df:')
    products_df.show()

    # результирующий датафрейм
    result_df = get_products_with_categories(products_df, categories_df)

    print('result_df:')
    result_df.show()

    spark.stop()

