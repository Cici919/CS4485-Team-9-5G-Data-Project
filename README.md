# 5G Data Analysis - Team 9 Performance Management

## Overview
UTDallas CS Project - Prof. Anand Gupta <br/>

This Performance Management project focuses on visualizing 5G performance data by integrating Prometheus for metric collection and Kafka for real-time data streaming.
The goal is to provide a powerful solution for monitoring 5G network performance through real-time key performance indicator (KPI) visualization,
with a special emphasis on downlink and uplink metrics. The system also ensures secure access via Auth0 for user authentication and dynamic 
dashboards powered by Prometheus for effective data visualization.

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
 Note: Make sure you have Auth0 access permission
   
### II. Code-After-Integration Branch (Full satck code from Team 7)
 1. Clone the project folder from the Code-After-Integration branch to your local machine.
 2. Ensure Docker Server is Running<br>
    Before running the project, ensure that your Docker server is up and running.<br>
    You can start your Docker server by clicking the shortcut on your desktop.
 4. Install Necessary Dependencies<br>
    Make sure all necessary dependencies and react-scripts are properly installed.<br>
    React-scripts is part of the Create React App setup and is essential for your React project.<br>
    Dependencies (such as JavaScript files, CSS files, or assets) guarantee your project to function correctly.<br>
    Run the following command to install dependencies:
*         npm instal
 4. Run the Project<br>
    Navigate to the project directory and run the following command<br>
    For the React Frontend(start the React development server):   
*         npm start
    For the Backend (Docker):<br>
    Navigate to the team9 folder (performance directory) and run the following command:
*         docker-compose up --build   
   Note: These two commands should be run in separate terminal windows or command prompts, but both should be in the same root project directory.
 5. Authentication Process<br>
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
*        docker-compose down
  
### III. prom-kafka Branch (Only Backend)
Follow the Readme file in prom-kafka branch to run the code.
## Challenges and Future Considerations<br>
Managing real-time data flow, ensuring smooth integration between Kafka, Prometheus, and Mage, and handling Auth0 authentication presented significant challenges. To address these, we utilized Dockerized environments and relied on comprehensive troubleshooting through documentation.

## Future Enhancements<br>
Looking ahead, incorporating predictive maintenance and infrastructure monitoring using machine learning is a potential area for further development, which could enhance the system’s capability to proactively detect and resolve network issues.
