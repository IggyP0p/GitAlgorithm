# GitAlgorithm

A graphical application built with **Python + Tkinter** that allows you to perform **Git commits** (GitHub, GitLab, or both) by executing Git commands directly in the system terminal using `subprocess`.

The goal of this project is to simplify the commit process without requiring the user to manually type Git commands.

---

## 🧩 Features

- Simple graphical interface built with Tkinter
- Local Git repository detection
- Commit creation via Git
- Support for:
  - GitHub
  - GitLab
- Visual feedback for success and error messages
- Execution of Git commands via terminal using `subprocess`

---

## ⚙️ Requirements

- **Operating System:** Linux  
  > ⚠️ This project was developed and tested only on Linux.  
  > There is no guarantee it will work on Windows.

- **Python:** 3.9 or higher (recommended)
- **Git** installed and properly configured
- **Tkinter** (usually included with Python)

---

## 🔐 Git Authentication (IMPORTANT)

For the program to work correctly:

- GitHub and/or GitLab repositories must already be created
- Your machine must be able to run `git commit` and `git push` **without requesting username or password**
- The **recommended authentication method is SSH**

📌 This program **does not handle authentication via token or password**.  
It assumes Git is already correctly configured on the system.
