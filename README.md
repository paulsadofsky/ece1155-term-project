Demonstration of Cyberattacks on a Password Protected Computer System

Nathaniel Ginck, Paul Sadofsky, Tiago Alfonso Wells, Johann Traum

Abstract

For our project, we are going to simulate a password-protected system that is undergoing cyberattacks. We are going to simulate password-cracking cyberattacks on a system to demonstrate how the time to crack increases as a parameter of password length, and character set. We expect time complexity to increase exponentially with password length, and we expect that as the password character set increases (including numbers and special characters) the time to brute force a password increases. The different rulesets for character inclusions are defined below:

Case 1: lowercase letters only

Case 2: lowercase and uppercase letters

Case 3: lowercase, uppercase letters, and numbers

Case 4: lowercase, uppercase letters, numbers, special characters

Special letters are defined as the following list: “!@#$%^&*()[]+=.,<>-_”. Case 1 consists of 26 characters, Case 2 consists of 52 characters, Case 3 consists of 62 characters, and Case 4 consists of 82 characters.
To accomplish this, we are splitting our project into two parts: a password generation side and a password cracking side. For generating a password, we will create a random password that is between eight and twelve characters in length, depending on the user’s choice. For the cracking, we will be implementing a brute forcing algorithm to generate passwords. Both the generated password and the cracking passwords will be generated according to the current parameter ruleset, which will be also decided by the user. Both of these will be completed in Python. Our end goal is to plot the time required to crack each password length (eight through twelve) for each ruleset of character inclusion. This will demonstrate the trends of password cracking difficulty for each ruleset as a function of password length.

Additionally, due to the high computational cost of running this algorithm, we will include simulated times once the password cracking code takes longer than an hour to run. These will be determined by calculating an average time to perform a guess, which will be taken over a short sample. This value, seconds per guess, will be multiplied by the number of combinations divided by two. This result is the average simulated time and is helpful for the exceptionally long computation times.
As a result of our tests, we found that password length is the most important factor when it comes to crafting a password that is well protected against brute force attacks due to the high computational resources and time necessary to execute such an attack successfully.
