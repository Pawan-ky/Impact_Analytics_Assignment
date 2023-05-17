# Impact_Analytics_Assignment

## Approach
There is always 2 possibilities either you attend the class or not attend the class.

So total no. of ways are 2^N (N is no.of days)

eg. A,P,AA,PP,AP,PA .... etc  (A - abset, P - Present)

Steps :- 
Calculate or generate the patterns to attend the classes

Next filter out all permutation which has 4 or more consecutive days of absence.

The filtered result is total no. ways one can attend classes.

Also count the ways in which he/she will be absent on last days (he/she'll miss the ceremony in those ways)

to compute probability divide last_day_absent_count with total_ways_attend count


## Usage
#### Python3 must be installed in the system

```
python main.py
```
It will ask you to enter No. of days, enter no.days and hit enter

### Time Complexity is 2^N (N = No. of days)
