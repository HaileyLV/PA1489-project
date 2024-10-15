# **Reflections 3**

## **1. Name of everyone in the team:**
    - Ebba Bengtsson
    - Hailey Lundkvist
    - Sabor Ahmad Khowajazada
    - Thanh Chu
    - Wilma Eriksson
## **2. Link to the project's page on the git server:**
https://github.com/HaileyLV/PA1489-project.git

## **3.Assignment:**
### *3.1. Short summary of which functionality you have tested:*
- **Test**: I use Pytest to test with some functions som contact to the database.
### *3.2. Short summary of how you have completed the test:*
- All my test failed in the beginning because I did not set up a function to connect to the database (with 4 test) and did not use the relative path from the BurgerOrderer forder to MenuStore (with 2 test). But they were all pass after I edited the codes.
### *3.3. Printout from your last test session, so you can see:*
- How many tests you have written: 6 tests
- What they test:
      + 4 test with database: I sat up a function to connect to the database in an other forder: def db_connection(), then tested if a table exist/not exist in database and test to create and drop a table in database.
      + 2 test with BurgerOrderer: tested function select_a_column and function index in BurgerOrderer. I used the relative path from the BurgerOrderer folder to MenuStore during this test.
- How many tests succeed or fail: all of them are succeed

### *3.4. Your experiences about writing automated unit tests:*
- What went well?: I know how to use Pytest and could write a few test case.
- What went less well?
- How did you solve the difficulties? Could you have done differently?
    + Our functions are grouped quite a lot so testing is also more difficult. I have splitted the function to make it easier to test and I could write two test with BurgerOrderer because of it.         
- What did you not manage to solve? Why not?
    + We started with assignment 3 very late. The time was too urgent so I could not perform as many test cases as expected. In the next project, we had to adjust the time estimate.
    + I wanted to test creating and sending orders to the database but out order_id is automatically generated, so I had not dared to try, afraid of conflicts.
    + My test in BurgerOrderer are all hard-code tests. It the user changes the details in database, my tests are no longer valid. I still do nor know if there is a way to fix these things.
### *3.5. Link to the documentation from your respective debug sessions in your individual engineering diarie:*
<https://github.com/HaileyLV/PA1489-project/blob/main/Engineer%20diary/Thanh%20Chu%20-%20engineer%20diary.md?plain=1>

