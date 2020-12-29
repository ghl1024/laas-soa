def load():
    with open("test.csv") as f:
        lines = f.readlines()

    max_columns = []
    columns = []
    result = {}
    for item in lines:
        item = item.strip()
        data = item.split(",")

        data_date = data[0]
        data_dbname = data[1]
        data_count = data[2]

        columns.append(data_dbname)
        if not result.__contains__(data_date):
            result[data_date] = {}
            if len(columns) > len(max_columns):
                max_columns = columns
            columns = []

        result[data_date][data_dbname] = data_count
    mtdl = 18  # max_table_data_len
    table_column_str = "date" + " " * (mtdl - len("date"))
    for item in max_columns:
        table_column_str += item + " " * (mtdl - len(item))
    print(table_column_str)
    table_data_str = ""
    result_keys = list(result.keys())
    for result_key in result_keys:
        value = result[result_key]
        table_data_str += result_key + " " * (mtdl - len(result_key))
        for max_columns_item in max_columns:
            value_temp = ""
            if value.__contains__(max_columns_item):
                value_temp = value[max_columns_item]
            table_data_str += value_temp + " " * (mtdl - len(value_temp))
        print(table_data_str)
        table_data_str = ""


if __name__ == '__main__':
    load()
