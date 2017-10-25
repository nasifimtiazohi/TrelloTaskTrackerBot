# Selenium Testing for Three usecases

## Overview
We conducted Selenium testing based on Chrome, and fixed the JUnit testing orders.
The four JUnit tests we haved conducted are 
 * "sendNaggingReminder"
 * "testEmailSent"
 * "performanceEvaluation"
 * "reminderBuddy"

## Usecase 1: Send Nagging Reminder
 * Test the following functionalities:
	 * Input "@firsttest usecase 1" command to slackbot
	 * Firsttest bot respond by sending the names of users who has task that is due within 1 day deadline
	 * Sends a Email to his/her email address
 * The test cases for this usecase are "sendNaggingReminder and "testEmailSent.
 	 * sendNaggingReminder
   *    Check if the bot respond the names of three persons who have task unfinished (based on our mock data)
   * testEmailSent
   *    Check if the email is sent to these person by checking the sender's gmail box with the timestamp same as the person input the command to the bot
 
 
## Usecase 2: Performance Evaluation
 * Test the following functionalities:
	 * Input "@firsttest usecase 2" command to slackbot
	 * Firsttest bot respond by sending the names of users as long as their performance score
 * The test case related to this usecase is "performanceEvaluation"
 	 * performanceEvaluation
   *    Check if the five users along with their score are printed by the bot
 
 
 ## Usecase 3: Reminder Buddy
 * Test the following functionalities:
	 * Input "@firsttest usecase 3" command to slackbot
	 * Firsttest bot respond by sending direct message to the person who has task unfinished
 * The test case related to this usecase is "reminderBuddy"
 	 * reminderBuddy
   *    check if the last sentence of the chat screen is "what is your progress, mate?"
 
