column_list = food_info.columns.tolist()
gram_columns = [col for col in column_list if col.endswith('(g)')]
gram_df = food_info[gram_columns]
gram_df.head(3)
