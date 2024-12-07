# 5G Data Analysis - Team 9

## Overview
UTDallas CS Project - Prof. Anand Gupta <br/>
Refer to the software requirements specification. <br/>
(To Do: add link to one pager)

## Team Members
* Chen Cheng
* Changyub Lee
* Hector Macias
* Ethan Sun

## Use Cases
1. Performance Metrics
2. Accounting Management

## Technologies Used
- **Docker** for containerization  
- **Node.js** for the frontend  
- **Kafka** for data generation and consumption  
- **Prometheus** for data scraping  
- **Mage.ai** for building and managing machine learning pipelines

## How to Run the Different Version of Code

### I. Main Branch (With simple Auth0 Authentication)
 1. Clone or copy the repository to your local machine.
 2. Open your command prompt or terminal.
 3. Navigate to the project directory where the docker-compose.yml file is located.
 4. Run the following command to build and start the containers:
 *     docker-compose up --build
 * Note: Make sure you have Auth0 access permission
   
### II. Code-After-Integration Branch (Full satck code from Team 7)
 1. Clone the project folder from the Code-After-Integration branch to your local machine.
 2. Ensure Docker Server is Running
    Before running the project, ensure that your Docker server is up and running.
    You can start your Docker server by clicking the shortcut on your desktop.
 4. Install Necessary Dependencies
    Make sure all necessary dependencies and react-scripts are properly installed.
    React-scripts is part of the Create React App setup and is essential for your React project.
    Dependencies (such as JavaScript files, CSS files, or assets) make sure your project to function correctly.
    Run the following command to install dependencies:
*   npm instal
 4. Run the Project
    Navigate to the project directory and run the following command
    For the React Frontend(start the React development server):   
*         npm start
    For the Backend (Docker):
    Navigate to the team9 folder (performance directory) and run the following command:
*        docker-compose up --build   
   Note: These two commands should be run in separate terminal windows or command prompts, but both should be in the same root project directory.
 5. Authentication Process
    Follow Team 7's Auth0 authentication process to authenticate users.
 6.   Access Performance Dashboard
      * After authentication, go to the interface and click on the Performance Management menu.
      * Click the Dashboard button.
      * Navigate to Prometheus UI.
      * You can query the status of any 5G network by typing the matrix name.
  7. Gracefully Shut Down.
     To shut down the servers gracefully, follow these steps:
     * To both command prompts and press Ctrl + C to stop the servers.
     * In the terminal where Docker is running, execute the following command to clean up the running services:
*      docker-compose down
  
### III. prom-kafka Branch (Only Backend)
Follow the Readme file in prom-kafka branch to run the code.

