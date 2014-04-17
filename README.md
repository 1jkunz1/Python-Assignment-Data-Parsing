Python-Assignment-Data-Parsing
==============================

Simple Python Program


Background: A research group has created an on-line training program that consists of 6 chapters. For 
each chapter, the user is required to read a .pdf file (OverView), watch a training video (Movie), read 
some articles (Articles), look at some clinical tools (Clinical), go through a FAQ document (FAQ), read 
some case studies (Case) and take a quiz (Quiz). If they have completed any of these components, a 
date is recorded. Quiz scores have been recorded, and quiz answers have also been stored. If they have 
completed all of the components for a chapter, the value for the variable “Complete” will be “YES”, and 
if any component is missing, the value for the variable “Complete” will be “NO”. 
If a user has completed all 6 modules, they are eligible to receive a certificate. If they are missing any 
one of the components of any one of the modules, they cannot receive credit. The data for each user is 
organized as follows: 
Name 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
Chapter XXXXX 
ALL data for Chapter XXXXX, not in any specific order, but all components are listed…somewhere 
in this section is the following : Complete: YES or Complete: NO 
ChapterDone 
UserDone 
 
The chapters are not in order, and the modules within each chapter are not in order, or in the same 
order from module to module. Also, the number of lines for each chapter is not constant. The only thing that is consistent is that the start of a block includes the word “Chapter” along with a number, and 
every chapter ends with the text “ChapterDone”. Every block for a user starts with the user name, and 
ends with the text “UserDone”. Each user will have information pertaining to all 6 modules (no missing 
blocks of information). 
 
Your task is to write a program that reads a text file containing data related to a group of users, and 
determines if any of the users have completed the training and can earn a certificate. I will provide a 
text file containing some sample data for you to test your program. 
How does this relate to discrete structures? Chapter 1 in our textbook discusses logic and reasoning. 
With this problem, you need to establish the logic for how to determine if a user has earned a certificate 
(and implement this logic). You have enough data to do in-depth analysis on the users, but at this point 
you are focusing on one simple component: has a user earned a certificate? You need to think about 
the information contained that is related to this problem, and ignore the irrelevant data. Because the 
number of lines related to each module is not consistent, you will need to come up with a strategy to 
automate checking the status of each user without relying on a simple iterative process. 
Here is an example of the data for a single user (clearly this user has not earned a certificate)…notice 
that Chapter 1 is complete, and has dates for the various components. Chapter 2 has had some 
progress, but is not complete, and Chapter 5 has not been attempted, so there are no dates: 
Average Joe 
Chapter4 
OverView: NO 
Case: NO 
FAQ: NO 
FakeScore: 0 
Movie: NO 
Articles: NO 
Clinical: NO 
Complete: NO 
QuizScore: 0 
ChapterDone 
Chapter3 
OverView: NO 
Case: NO 
FAQ: NO 
FakeScore: 0 
Movie: NO 
Articles: NO 
Clinical: NO 
Complete: NO 
QuizScore: 0 ChapterDone 
Chapter2 
Clinical: YES 
Articles: YES 
Complete: NO 
ClinicalDate: 2012-07-05 01:01:51 PM 
CaseDate: 2012-07-10 11:34:56 AM 
OverViewDate: 2012-07-05 02:25:23 PM 
FAQDate: 2012-07-10 11:35:18 AM 
MovieDate: 2012-07-27 10:24:23 AM 
ArticlesDate: 2012-07-05 01:44:43 PM 
OverView: YES 
QuizScore: 0 
FAQ: YES 
Movie: YES 
FakeScore: 0 
Case: YES 
ChapterDone 
Chapter6 
OverView: NO 
Case: NO 
FAQ: NO 
FakeScore: 0 
Movie: NO 
Articles: NO 
Clinical: NO 
Complete: NO 
QuizScore: 0 
ChapterDone 
Chapter1 
Clinical: YES 
Articles: YES 
Complete: YES 
ClinicalDate: 2012-07-05 09:10:59 AM 
CaseDate: 2012-07-05 09:10:58 AM 
OverViewDate: 2012-07-05 09:27:48 AM 
QuizAnswers: 11101 
FAQDate: 2012-07-05 09:10:52 AM 
MovieDate: 2012-07-05 10:04:01 AM 
QuizDate: 2012-07-05 01:01:44 PM 
ArticlesDate: 2012-07-05 09:10:46 AM 
OverView: YES QuizScore: 4 
StartDate: 2012-07-05 12:59:44 PM 
FAQ: YES 
Movie: YES 
FakeScore: 5 
Case: YES 
ChapterDone 
Chapter5 
OverView: NO 
Case: NO 
FAQ: NO 
FakeScore: 0 
Movie: NO 
Articles: NO 
Clinical: NO 
Complete: NO 
QuizScore: 0 
ChapterDone 
UserDone 
