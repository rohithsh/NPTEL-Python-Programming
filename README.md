# NPTEL-Python-Programming
**Programming, Data Structures And Algorithms Using Python** conducted by IIT Madras as a part of NPTEL.  
Batch: Feb - Mar 2020  
Duration: 8 Weeks  
All answers were submitted by me as a part of *Weekly Programming Assignments* given to enrolled students during the course.
## Programming Assignment Answers
### 4.1 ORANGE CAP
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:
```
{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
```  
Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.  
Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.  
**Sample Input**
```
orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
```
**Sample Output**
```
('player3', 100)
```  
### 4.2 and 4.3 ADDPOLY and MULTPOLY
Let us consider polynomials in a single variable x with integer coefficients. For instance:
```
3x4 - 17x2 - 3x + 5
```
Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.  
We have the following constraints to guarantee that each polynomial has a unique representation:  
  - Terms are sorted in descending order of exponent
  - No term has a zero cofficient
  - No two terms have the same exponent
  - Exponents are always nonnegative
  
For example, the polynomial introduced earlier is represented as:  
```
[(3,4),(-17,2),(-3,1),(5,0)]
```
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.  
Write Python functions for the following operations:
```
addpoly(p1,p2)
multpoly(p1,p2)
```
**Sample Input 1**  
```
addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
```
**Sample Output 1**
```
[(2, 1),(3, 0)]
```
**Explanation 1**
```
(4x^3 + 3) + (-4x^3 + 2x) = 2x + 3
```
**Sample Input 2**  
```
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
```
**Sample Output 2**
```
[(1, 3),(-1, 0)]
```
**Explanation 2**
```
(x - 1) * (x^2 + x + 1) = x^3 - 1
```
### 5.1 HOGWARTS LIBRARY
The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.  
Information about books  
Line format: Accession Number\~Title  
Information about borrowers  
Line format: Username\~Full Name  
Information about checkouts  
Line format: Username\~Accession Number\~Due Date  
**Note: Due Date is in YYYY-MM-DD format.**    
You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.  
Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.  
Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one currently issued book in the following format:  
 **Due Date\~Full Name\~Accession Number\~Title**  
Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name. If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.  
 **Sample Input**
```Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput
```
**Sample Output**
```2019-03-14~Katie Bell~APM-002~Advanced Potion-Making
2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory
2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls
2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls
2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory
```
