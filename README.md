# assignment-3
Assignment 3 of Training and Placement. Improvement over the previous management system with quiz features.

### Features
- Registration functionality (Atleast 10 fields for data)
- Login/logout functionailty (through username, password)
- Show/Update profile
- Quizes
- Admin Profile (Password is Hardcoded)
- Persistent storage (using Pickle)
- Menu Based Navigation

### New Feature: Quizes

- After logging-in to the program, students can take quizes for any three subjects (DSA, DBMS or Python)
- Questions are fetched from `questionaire.json` and randomly asked.
- After the Quiz, The score is updated. If the student has scored lass than their previous score, the scores are not updated.
- Quiz scores can be seen in `Show Profile` option.
- The Admin can view scores for all students in one tabular format.
