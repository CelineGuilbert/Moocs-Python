##1. Read
import pandas

food_info = pandas.read_csv("food_info.csv")
col_names=food_info.columns.tolist()


##2: Transforming A Column
sodium_grams = food_info['Sodium_(mg)'] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

##3: Performing Math With Multiple Columns
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron=food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]


##4.Creating a nutritional index
Score=2×(Protein_(g))−0.75×(Lipid_Tot_(g))
weighted_protein = food_info['Protein_(g)'] * 2
weighted_fat = food_info["Lipid_Tot_(g)"] * -0.75
initial_rating = weighted_protein+weighted_fat


##5: Normalizing Columns In A Data Set
#The columns in the data set use different units (kilo-calories, milligrams, etc.)
#While there are many ways to normalize data, one of the simplest ways is to divide all of the values in a column by that column's maximum
#value. This way, all of the columns will range from 0 to 1

max_protein = food_info["Protein_(g)"].max()
normalized_protein= food_info["Protein_(g)"]/max_protein

max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat= food_info["Lipid_Tot_(g)"]/max_fat

##6: Creating A New Column
food_info["Normalized_Protein"] = normalized_protein ##add column Normalized_Protein
food_info["Normalized_Fat"] = normalized_fat

##7: Create A Normalized Nutritional Index
food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

food_info['Norm_Nutr_Index'] = (food_info["Normalized_Protein"]  *2) + (-0.75 * food_info["Normalized_Fat"])

##8: Sorting A DataFrame By A Column
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
# DataFrame objects have a sort_values() method that we can use to sort the entire DataFrame.
food_info.sort_values("Sodium_(mg)")
#pour aller plus loin
# Sorts the DataFrame in-place, rather than returning a new DataFrame.
food_info.sort_values("Sodium_(mg)", inplace=True)

# Sorts by descending order, rather than ascending.
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)

