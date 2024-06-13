import pandas as pd

# Read the CSV file
df = pd.read_csv(r"../Imputation_Results/Imputation_noRestoring_Results/EV_Vehicles/2/EV_Vehicles_4000_12000_2.csv", sep=';')
df = df.drop(['riga'], axis=1)
print(df.columns.tolist())

# Initialize counters
not_imp = 0
exact = 0
similar = 0
tot = 0

# Define tolerances for the attributes
tolerances = {
    "city": None,  # No tolerance specified for city attribute
    "addr": None,  # No tolerance specified for addr attribute
    "name": None,  # No tolerance specified for name attribute
    "phone": None,  # No tolerance specified for phone attribute
    "class": 0,  # Tolerance of 0 specified for class attribute
    "type": None  # No tolerance specified for type attribute
}

# Values to be considered similar for certain attributes
similar_values = {
    "city": [
        ["los angeles", "la", "santa monica", "w. hollywood", "hollywood", "westwood", "beverly hills", "malibu", "sherman oaks", "long beach", "redondo beach", "venice"],
        ["new york", "ny", "new york city", "queens", "brooklyn"]
    ],
    "addr": [
        ["239 w. broadway  between walker and white sts.", "239 w. broadway"],
        ["2637 peachtree rd. ne", "2637 peachtree rd.  peachtree house condominium"],
        ["2355 peachtree rd.  peachtree battle shopping center", "2355 peachtree rd. ne"],
        ["804 northpoint", "804 north point st."],
        ["95 ave. a at 6th st.", "95 ave. a"],
        ["1110 3rd ave. at 65th st.", "1110 third ave."],
        ["854 7th ave.  between 54th and 55th sts.", "854 seventh ave."],
        ["255 courtland st.  at harris st.", "255 courtland st."],
        ["595 piedmont ave.  rio shopping mall", "595 piedmont ave."],
        ["156 second ave.", "156 2nd ave. at 10th st."],
        ["293-b peachtree rd.", "b peachtree rd."],
        ["129 fremont st.", "129 e. fremont st."],
        ["2290 peachtree rd.  peachtree square shopping center", "2290 peachtree rd."],
        ["3073 piedmont rd.", "3073 piedmont road"],
        ["435 s. la cienega blv.", "435 s. la cienega blvd."],
        ["60 w. 55th st.  between 5th and 6th ave.", "60 w. 55th st."],
        ["8358 sunset blvd. west", "8358 sunset blvd."],
        ["1972 n. hillhurst ave.", "1972 hillhurst ave."],
        ["3rd st.", "8638 w. third st."],
        ["2450 broadway  between 90th and 91st sts.", "2450 broadway"],
        ["2 harrison st.  near hudson st.", "2 harrison st."],
        ["42 e. 20th st.  between park ave. s and broadway", "42 e. 20th st."]
    ],
    "name": [
        ["yujean kang's", "yujean kang's gourmet chinese cuisine"],
        ["spago", "spago (los angeles)"],
        ["pano's & paul's", "pano's and paul's"],
        ["philippe the original", "philippe's the original"],
        ["fenix", "fenix at the argyle"],
        ["hotel bel-air", "bel-air hotel"],
        ["grill on the alley", "grill  the"],
        ["le chardonnay", "le chardonnay (los angeles)"],
        ["palm  the (los angeles)", "the palm"],
        ["four seasons grill room", "four seasons"],
        ["lespinasse (new york city)", "lespinasse"],
        ["park avenue cafe", "park avenue cafe (new york city)"],
        ["coyote cafe", "coyote cafe (las vegas)"],
        ["le montrachet", "le montrachet bistro"],
        ["second street grille", "second street grill"],
        ["steak house", "steak house  the"],
        ["tillerman  the", "tillerman"],
        ["bone's", "bone's restaurant"],
        ["ciboulette", "ciboulette restaurant"],
        ["hedgerose heights inn", "hedgerose heights inn  the"],
        ["cafe  ritz-carlton  buckhead", "ritz-carlton cafe (buckhead)", "ritz-carlton dining room (buckhead)"],
        ["restaurant  ritz-carlton  atlanta", "ritz-carlton restaurant"],
        ["lulu restaurant-bis-cafe", "lulu"],
        ["mifune japan center  kintetsu building", "mifune"],
        ["ritz-carlton restaurant and dining room", "ritz-carlton dining room (san francisco)"]
    ],
    "phone": None  # No similar values specified for phone attribute
}

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    tot += 1
    if row['valore imputato'] == "?":
        not_imp += 1
    elif row['valore imputato'] == row['valore da imputare']:
        exact += 1
    else:
        attribute_name = row['nome attributo']
        if attribute_name in tolerances:
            if tolerances[attribute_name] is not None:
                original_value = float(row['valore da imputare'])
                imputed_value = float(row['valore imputato'])
                diff = abs(original_value - imputed_value)
                if diff <= tolerances[attribute_name]:
                    similar += 1
            elif attribute_name in similar_values:
                original_value = row['valore da imputare']
                imputed_value = row['valore imputato']
                if original_value.lower() in similar_values[attribute_name]:
                    if imputed_value.lower() in similar_values[attribute_name]:
                        similar += 1
            elif attribute_name == "phone":
                original_phone = row['valore da imputare']
                imputed_phone = row['valore imputato']
                original_phone_digits = ''.join(filter(str.isdigit, original_phone))
                imputed_phone_digits = ''.join(filter(str.isdigit, imputed_phone))
                if original_phone_digits == imputed_phone_digits:
                    similar += 1


# Calculate wrong imputations
wrong = tot - (not_imp + exact + similar)

# Print the results
print("Non Imputati:", not_imp)
print("Esatti:", exact)
print("Simili:", similar)
print("Esatti+Simili:", exact + similar)
print("Imputazioni totali:", exact + similar + wrong)
print("MV Totali:", tot)
print("Sbagliati:", wrong)
accuracy = (exact + similar) / tot
print("Accuracy:", accuracy)
precision = (exact + similar) / (exact + similar + wrong)
print("Precision:", precision)