# XLSX to CSV file converter

Python script that converts all the sheets of xlsx file(Google Sheet) into csv files.

Assumption: There is a single header row in all sheets of xlsx document

Input:
```sh
$ python converter.py google_sheet_link/local_file_location
```

Output:
dir_name(same as input file name)/
- Sheet 1.csv
- Sheet 2.csv
- …
- Sheet n.csv

E.g.
Input:
```sh
$ python converter.py Sample_Data - Python Assignment
```

Output:
Sample_Data - Python Assignment/
- Office Supply Sales.csv
- Food Sales.csv