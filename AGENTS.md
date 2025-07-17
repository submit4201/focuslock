# FocusLock - End-to-End Context and Development Guide

## Overview

FocusLock is a cross-platform desktop productivity tool written in Python. It helps users stay focused on their tasks by:

*   Triggering lockdowns around critical reminders/tasks
*   Blocking distracting apps and websites
*   Forcing the completion of key objectives to unlock the system
*   Surviving reboots and delays
*   Saving state and logging behavior for accountability

## Running the Application

To run the application, execute the following command from the root directory:

```bash
python -m focuslock.app
```

## Running Tests

To run the test suite, execute the following command from the root directory:

```bash
python -m unittest discover focuslock/tests
```

## Project Structure

```
focuslock/
├── app.py                    # Entry point
├── config/
│   └── settings.json         # Whitelist, lock times, preferences
├── core/
│   ├── scheduler.py          # Reminder scheduling logic
│   ├── locker.py             # System lock enforcement
│   ├── process_killer.py     # App monitor and killer
│   ├── whitelist_manager.py  # Manage allowed apps/sites
│   ├── watchdog.py           # Background monitor + reboot handler
│   └── startup_manager.py    # Auto-launch on boot
├── models/
│   ├── reminder.py           # Reminder model
│   ├── task.py               # Task/Objective model
│   ├── lockstate.py          # Lock session state
├── ui/
│   ├── lockscreen.py         # Fullscreen UI during lock
│   └── reminder_form.py      # Add/edit reminders
├── db/
│   └── database.py           # SQLite/TinyDB wrapper
├── utils/
│   ├── logger.py             # Logging + error capture
│   └── system.py             # OS detection, path helpers
└── tests/
    └── ...                   # Unit + integration tests
```
