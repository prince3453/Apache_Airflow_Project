# Apache_Airflow_Project Installation

- creating the python virtual environment
  - python3 -m venv venv

- Activate virtual environment
  - source venv/bin/activate

- Specify where we will store the confug file and metadatafiles
  - export AIRFLOW_HOME = /c/path/

- Download the constraints file
  - wget https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-2.9.1.txt

- Install airflow with constraints file
  - pip install "apache-airflow==2.9.1" --constraint constraints-2.9.1.txt

- Initialize database
  - airflow db init (mostly sqlite for the db)

- create an admin user
  - airflow users create --username admin --password ******(whichever you want but remember it) --firstname prince --lastname gp \
    -- role admin \
    -- email p**********@gmail.com 

- run the webserver and scheduler
  - airflow webserver --port 8080
  - airflow scheduler



## Components of Airflow
![airflow_comonents](https://github.com/prince3453/Apache_Airflow_Project/assets/47770221/aa600276-840b-4865-8fd7-6e043db5317a)

## DAGs information
![DAG](https://github.com/prince3453/Apache_Airflow_Project/assets/47770221/228e9f2d-79b1-4651-abc6-acf431ff6d49)

## process of the data pipelines
![process_flow](https://github.com/prince3453/Apache_Airflow_Project/assets/47770221/3d9c7634-61e4-449f-8c92-0687a114675c)

## Procedure and framworks can be used as a platform
![looks_datapipeline](https://github.com/prince3453/Apache_Airflow_Project/assets/47770221/21c83b66-ac2a-49ae-8d64-4a43000e8217)


Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://docs.astronomer.io/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://docs.astronomer.io/cloud/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.


CLI commands for airflow
====

Shows every container : docker ps -s
Now take the Container ID for the web service 

Exececute the following docker command:
- docket exec -it e060438075ad  /bin/bash

Then after every time you can use following command as we are using the astro CLI
- astro dev bash


Most important CLI for database

This is use to check the data available in airflow
- airflow db check

This is use to clean the data
- airflow db clean 

Export the archived data to csvfile
- airflow db export-archived

Export the archived data to csvfile
- airflow db export-archived

Drop the archived data
- airflow db drop-archived

Intiate the airflow (if we are not using the astro or any other type of airflow runnner)
- airflow db init

run the specified task during the specified range of date
- airflow dags backfill mydag --reset-dagrun --rerun-failed-tasks --run-backwards -s 2024-01-07 -e 2024-10-07

Re-synce dags
- airflow dags reserialize

list of all dags
- airflow dags list

Task instance testing
- airflow tasks test mydag mytask 2024-01-07

To know about all the commands of airflow
- airflow cheat-sheet


# task dependencies:

- taskA >> taskB
 - here the taskA is upstream for taskB and taskB is the Downstream for the taskA