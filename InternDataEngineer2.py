from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def get_product_category_pairs_with_empty_categories(products_df, categories_df):
    # Объединяем датафреймы продуктов и категорий по полю 'product_id'
    joined_df = products_df.join(categories_df, products_df.product_id == categories_df.product_id, 'left_outer')

    # Выбираем нужные столбцы и переименовываем их для читаемости
    selected_df = joined_df.select(products_df.product_name.alias('Product'), categories_df.category_name.alias('Category'))

    # Создаем новый столбец, который содержит 1, если категория не задана, и 0 в противном случае
    selected_df = selected_df.withColumn('No_Category', when(col('Category').isNull(), 1).otherwise(0))

    # Получаем все пары "Имя продукта - Имя категории"
    product_category_pairs = selected_df.select('Product', 'Category')

    # Получаем имена всех продуктов, у которых нет категорий
    products_with_no_categories = selected_df.filter(col('No_Category') == 1).select('Product')

    return product_category_pairs, products_with_no_categories

# Пример использования
if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    # Пример данных
    products_data = [("product1", "product1_desc", 1), ("product2", "product2_desc", 2)]
    categories_data = [("product1", "category1"), ("product1", "category2")]

    # Создаем датафреймы
    products_df = spark.createDataFrame(products_data, ["product_id", "product_name", "product_value"])
    categories_df = spark.createDataFrame(categories_data, ["product_id", "category_name"])

    # Получаем результат
    product_category_pairs, products_with_no_categories = get_product_category_pairs_with_empty_categories(products_df, categories_df)

    # Выводим результаты
    print("Product-Category Pairs:")
    product_category_pairs.show()
    print("\nProducts with No Categories:")
    products_with_no_categories.show()

    spark.stop()
