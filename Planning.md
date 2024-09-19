# Planning
## 1. Form development team:
- Plan how you want to work: We sit together at least twice a week: Tuesday (after class) and Thursday (after the lab)

# 2. Determine development environment
- We use VS code.

# 3. Decide which git server you want to use
- Github
- We all have our own accounts on Github

# 4. Language:
- Python

# 5. Our products must have these features:
- A container-based platform, with separate containers for BurgerOrderer, KitchenView, and MenuStore.
**BurgerOrderer:** The main web interface. No need to make it fancy. Functionality is most important.
- Presents the different product types
- The customer can choose what they want to include in their order
- Customer **can customize their order** (eg remove “onions” from their “Metric Ton Bacon Burger”)
- Retrieves information about the different product types from the MenuStore database
- When the order is ready, it is sent via a REST call to KitchenView

**MenuStore**: A database that contains information about each type of item.
- Information about the different product types and how to customize them can be managed via a separate interface such as **admins**

**KitchenView**: Receives orders from BurgerOrderer and displays them to the kitchen staff.
- When an order is received via a REST API, it must be printed on the screen.
- Just need a simple text based printout.

# 5. Weekly plan:
## Week 35+36
- Create a team of 5 members.
- Meet 1 to introduce the team.
- Hailey created a project on Github and shared to everyone.

## Week 37:
- Learn about product design.
- Agree on programming language (Python), environment (VS code), gitserver (Github) and preliminary work division.
- Draft design:
  <https://app.moqups.com/CNsCqWOjxAXBnT1q7BVJIuRvwCjqD6zl/view/page/ad64222d5>
## Week 38:
- Learn about Flask and download the software.
- Practice pulling and pushing data from each person's computer to Github.
- Code BurgerOrderer and KitchenView

## Week 39:
- Learn about Flask. Link: <https://www.geeksforgeeks.org/flask-creating-first-simple-application/>
- Code BurgerOrderer and KitchenView, write documents.
- Update Engineer diary
## Week 40:
- Product assembly and testing the first time
- Fix bug, update Engineer diary
- Code MenuStore and write document of MenuStore
- Update Engineer diary
## Week 41:
- Product assembly and testing the second time
- Fix bug, write
- Update Engineer diary
## Week 42:
- Product assembly and testing the third time
- Fix bug, write
- Update Engineer diary
## Week 43:
- Product release
- Update Engineer diary
- Write Reflektioner
## Week 44:
- Check all again before submit
