### Value_Inc_Python_Cleaned_Data

This is a Python script that takes Value Inc.’s retail transaction data, tidies it up, and adds extra useful info so it’s ready for a Tableau dashboard. It works out important business numbers, pulls out client details, and mixes in seasonal info so the final file is all set for analysis.

### What the code does:

1. Opens the data files using Pandas.


2. Works out profit, sales, cost, markup, and combines dates into one column.


3. Pulls out client age, type, and contract length from the ClientKeywords column.


4. Joins the main data with a file that shows which season each month falls into.


5. Saves the cleaned-up data as a new CSV file you can drop straight into Tableau.