# Assignment 2 - Text Encryption and Decryption

## Group Members
- Subha Sitaula
- Diksha
- Pawan Acharya
- Esha 

## Description
**Q1.** This program takes text from a file (raw_text.txt), then encrypts the text using two-user supplied shifts (shift1 and shift2) and saves the resulting text in encrypted_text.txt

It then decrypts the text and saves it in decrypted_text.txt, then crosschecks it with the original file.

This indicates that the processed text during encryption and the processed text during decryption is unchanged and therefore the encryption and decryption process is accurate.

## Encryption Rules
The program uses the following rules for letter shifts:

**Lowercase letters:**

a-m = shift forward by shift1 * shift2

n-z = shift backward by shift1 + shift2

**Uppercase letters:**

A-M = shift backward by shift1

N-Z = shift forward by shift2^2

**Other characters:**

Spaces, numbers, tabs and punctuation are unchanged.

## Program Behavior

1) When the program is executed:

2) The user asked for shift1 and shift2

3) The program reads raw_text.txt.

4) An encrypted version is saved as encrypted_text.txt.

5) A decrypted version is saved as decrypted_text.txt.

6) The program indicates whether, and how many, the original text and decrypted text differences.

## Screenshot of Program Output
<img width="1176" height="922" alt="image" src="https://github.com/user-attachments/assets/9141ab4b-2771-470c-ae95-68b980aa4b8f" />
<img width="1724" height="612" alt="image" src="https://github.com/user-attachments/assets/0f603a01-1e32-460b-9ec6-edfbb3bc3a99" />
<img width="1787" height="587" alt="image" src="https://github.com/user-attachments/assets/d67824c3-161b-4579-9378-99738b5629c1" />

**Q2.** This program reads temperature data from many CSV files stored in the temperatures/ folder (each file is one year). It ignores missing values and performs three analyses across all stations and all years:
Seasonal Average — average temperature for each Australian season (Summer, Autumn, Winter, Spring). Results saved to average_temp.txt.

Temperature Range — station(s) with the largest temperature range (max − min). Results saved to largest_temp_range_station.txt.

Assumptions
All CSV files are inside the temperatures/ folder.
Each CSV file has at least these columns: Station, Date, Temperature.
Date can be in any standard format readable by pandas.to_datetime.
Temperature is numeric; missing values may be present and should be ignored.
Australian seasons mapping:
Summer: December, January, February (12, 1, 2)
Autumn: March, April, May (3, 4, 5)
Winter: June, July, August (6, 7, 8)
Spring: September, October, November (9, 10, 11)
Files Produced
average_temp.txt
Example line: Summer: 28.5°C
largest_temp_range_station.txt
Example line: Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)
If multiple stations tie, each is listed on its own line.
temperature_stability_stations.txt
Example lines:
Most Stable: Station XYZ: StdDev 2.3°C
Most Variable: Station DEF: StdDev 12.8°C
If multiple stations tie for stable/variable, list them all.
Program Behavior (what happens when you run it)
The program reads all .csv files from the temperatures/ folder.
It converts Date to month numbers and maps each record to an Australian season.
It ignores NaN temperature values in all calculations.
It computes:
Seasonal averages across all stations and years (writes average_temp.txt).
Per-station min, max, and range; finds station(s) with largest range (writes largest_temp_range_station.txt).
Per-station standard deviation; finds most stable (min std) and most variable (max std) stations (writes temperature_stability_stations.txt).
All results are saved to the files listed above.
 
## Screenshot of Program Output
<img width="1149" height="705" alt="image" src="https://github.com/user-attachments/assets/e904636e-051c-421b-a256-f60a83d1b3fa" />
<img width="1159" height="713" alt="image" src="https://github.com/user-attachments/assets/168ab6c1-7bbf-44c5-989f-bd15d3b27544" />
<img width="1154" height="713" alt="image" src="https://github.com/user-attachments/assets/dd0f1f87-dcab-4aaf-8943-410a954200f6" />

