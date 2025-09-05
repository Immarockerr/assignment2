# Assignment 2 - Text Encryption and Decryption

## Group Members
- Subha Sitaula 
- Diksha
- Pawan Acharya
- Esha 

## Description
This program takes text from a file (raw_text.txt), then encrypts the text using two-user supplied shifts (shift1 and shift2) and saves the resulting text in encrypted_text.txt

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

**1)** When the program is executed:

**2)** The user asked for shift1 and shift2

**3)** The program reads raw_text.txt.

**4)** An encrypted version is saved as encrypted_text.txt.

**5)** A decrypted version is saved as decrypted_text.txt.

**6)** The program indicates whether, and how many, the original text and decrypted text differences.

## Screenshot of Program Output
<img width="940" height="737" alt="image" src="https://github.com/user-attachments/assets/e1685b00-9361-4fe1-8e71-cb19cf8d1fc9" />
<img width="940" height="334" alt="image" src="https://github.com/user-attachments/assets/38eced22-995c-4d37-ab8e-47887741a6a2" />




## Q2. This program reads temperature data from many CSV files stored in the temperatures/ folder (each file is one year). It ignores missing values and performs
three analyses across all stations and all years:
**1)** Seasonal Average — average temperature for each Australian season (Summer, Autumn, Winter, Spring). Results saved to average_temp.txt.
   
**2)** Temperature Range — station(s) with the largest temperature range (max − min). Results saved to largest_temp_range_station.txt.
   
**3)** Temperature Stability — station(s) with the smallest and largest standard deviation (most stable and most variable). Results saved to temperature_stability_stations.txt.
   
# Assumptions

-All CSV files are inside the temperatures/ folder.

-Each CSV file has at least these columns: Station, Date, Temperature. -Date can be in any standard format readable by pandas.to_datetime. Temperature is numeric; missing values may be 

present and should be ignored.

-Australian seasons mapping: -Summer: December, January, February (12, 1,2) -Autumn: March, April, May (3, 4, 5) -Winter: June, July, August (6, 7, 8) -Spring: September, October, 

 November (9, 10, 11)
 
-Files Produced -average_temp.txt -Example line: Summer: 28.5°C -largest_temp_range_station.txt -Example line: Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C) -If multiple stations

tie, each is listed on its own line. -temperature_stability_stations.txt -Example lines: -Most Stable: Station XYZ: StdDev 2.3°C -Most Variable: Station DEF: StdDev 12.8°C -If multiple

stations tie for stable/variable, list them all.

## Program Behavior (what happens when you run it)

**1)** The program reads all .csv files from the temperatures/ folder.

**2)** It converts Date to month numbers and maps each record to an Australian season.

**3)** It ignores NaN temperature values in all calculations.

**4)** It computes:
-Seasonal averages across all stations and years (writes average_temp.txt).

-Per-station min, max, and range; finds station(s) with largest range (writes largest_temp_range_station.txt).

-Per-station standard deviation; finds most stable (min std) and most variable (max std) stations (writes temperature_stability_stations.txt).

**5)** All results are saved to the files listed above.

## Screenshot of Program Output
<img width="1149" height="731" alt="image" src="https://github.com/user-attachments/assets/cf6f26ba-ee2c-4c3d-a2b5-db3325bef7af" />
<img width="1146" height="574" alt="image" src="https://github.com/user-attachments/assets/e277787d-dadc-4a36-ad45-7c8b6513f38d" />
<img width="1145" height="582" alt="image" src="https://github.com/user-attachments/assets/dcd4d18e-1f42-4b8c-aa51-7a5d7db3fd0a" />
<img width="1148" height="623" alt="image" src="https://github.com/user-attachments/assets/6c4746bb-1ba9-4d0e-9ef5-1c5cc54ebe44" />

## Q3. Recursive Geometric Pattern Using Turtle Graphics
This program uses Python’s turtle graphics to generate a recursive geometric pattern that starts with a regular polygon and modifies its edges according to a recursive rule.

## Pattern Generation Rules

**1)** Each edge of the polygon is divided into three equal segments.

**2)** The middle segment is replaced with two sides of an equilateral triangle pointing inward (an indentation).

**3)** This transforms one straight edge into four smaller edges, each one-third the length of the original.

**4)** The process is applied recursively to each new edge based on the user-specified recursion depth.

## Example Behavior'

- Depth 0 ¬→ Straight edge with no modification.
  
- Depth 1 ¬→ Edge becomes four smaller edges with one indentation.
  
- Depth 2 ¬→ Each of the 4 edges gets one indentation and so on.
  
## User Input Parameters

- Number of sides → Determines the initial polygon (e.g., 3 = triangle, 4 = square).

- Side length → Length of each edge in pixels.

- Recursion depth → Number of recursive steps to apply.

## Program Behavior (when executed)

**1)** The user is prompted to enter:

   -Number of sides

   -Side length

   -Recursion depth

**2)** A polygon is drawn using turtle graphics.

**3)** The recursive indentation rules are applied to each edge until the given depth is reached.

**4)** The final geometric pattern is displayed in a new window.

## Screenshot of Program Output

<img width="940" height="498" alt="image" src="https://github.com/user-attachments/assets/732ddcf4-ab0a-4ce5-969f-4338109b54fe" />


