# Scheduler

A simple command-line tool for managing your projects, tasks, and notes. Stay organized and keep track of your work with an interactive CLI.

## Features

-   **Project Management**: Create and manage projects.
-   **Task Tracking**: Add tasks to projects with details like descriptions, status, priority, and due dates.
-   **Annotations**: Add notes or comments to your tasks.
-   **Interactive CLI**: An easy-to-use interactive command-line interface.
-   **Reporting**: View lists of your projects, tasks, and annotations.

## Getting Started

To start using Scheduler, run the main script from your terminal:

```bash
python3 scheduler.py
```

This will launch the interactive command-line interface.

## Commands

The scheduler provides several commands to manage your data.

### Add operations

-   `add project name=<project_name> description=<description>`: Creates a new project.
-   `add task project=<project_name> name=<task_name> description=<description> [due=<due_date>]`: Adds a new task to a project.
-   `add anno task=<task_name> description=<description>`: Adds an annotation to a task.

### Get operations

-   `list project`: Displays a list of all projects.
-   `list task`: Displays a list of all tasks.
-   `list anno [task=<task_name>]`: Displays annotations. If a task name is provided, it shows annotations for that specific task.
-   `show project=<project_name>`: Shows detailed information about a specific project and its tasks.
-   `show task=<task_name>`: Shows detailed information about a specific task and its annotations.

## TODO

* Update and delete functionalities.
* set default project/task.
* viewing task/project more efficiently.

