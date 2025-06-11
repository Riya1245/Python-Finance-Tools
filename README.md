# My Python Finance Tools

This project is a collection of various financial tools designed to operate via both Command-Line Interface (CLI) and Graphical User Interface (GUI). It includes a Currency Converter and an Expense Tracker.

---

## Features

* **Currency Converter:**
    * Facilitates currency exchange through a Command-Line Interface (CLI).
    * Offers an intuitive currency conversion experience via a Graphical User Interface (GUI).
    * Uses static exchange rates (you can extend this to integrate with a real-time API).

* **Expense Tracker:**
    * Allows adding, viewing, and tracking expenses via a Command-Line Interface (CLI).
    * Securely stores your expense data in an `expenses.csv` file (or `expenses.json` if configured).
    * Ability to plot visual representations (pie charts and bar charts) of your expenses.

---

## Requirements

To successfully run this project on your computer, you will need Python 3.x and a few essential Python libraries.

1.  **Python 3.x:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).
2.  **Required Python Libraries:** You'll need to install `requests` (if you plan to use a currency API) and `matplotlib` (for plotting expenses).
    Install them by running this command in your Command Prompt (or VS Code's integrated terminal):
    ```bash
    pip install requests matplotlib
    ```

---

## How to Run

Follow these steps to download and run the project on your computer:

1.  **Download the Project:**
    * Go to this GitHub repository page.
    * Click the **`<> Code`** button (it's usually green).
    * Select **"Download ZIP"**.
    * Once downloaded, unzip the file into a folder on your computer (e.g., `Python-Finance-Tools-main`).

2.  **Open Command Prompt/Terminal:**
    * Open the folder where you unzipped the project (e.g., `Python-Finance-Tools-main`) in your File Explorer.
    * Click on the address bar at the top of the folder (where the folder path is displayed).
    * Type **`cmd`** and press **Enter**. A Command Prompt window will open directly in that folder.

3.  **Run the Programs:**
    From the Command Prompt, you can run different programs using these commands:

    * **Currency Converter (CLI):**
        ```bash
        python cli_converter.py
        ```
        *Input example: amount (e.g., `100`), source currency code (e.g., `USD`), target currency code (e.g., `INR`)*

    * **Currency Converter (GUI):**
        ```bash
        python gui_converter.py
        ```
        *This will open a new GUI window for interaction.*

    * **Expense Tracker (CLI):**
        ```bash
        python cli_expense_tracker.py
        ```
        *This will display a menu where you can add, view, and plot expenses.*

---

## File Structure

The project folder structure is as follows:

Alright, no problem! Here's the README.md content in English for your GitHub repository.

Content for your README.md file (English)
Open your README.md file in VS Code and copy-paste this text. Remember to save the file after pasting.

Markdown

# My Python Finance Tools

This project is a collection of various financial tools designed to operate via both Command-Line Interface (CLI) and Graphical User Interface (GUI). It includes a Currency Converter and an Expense Tracker.

---

## Features

* **Currency Converter:**
    * Facilitates currency exchange through a Command-Line Interface (CLI).
    * Offers an intuitive currency conversion experience via a Graphical User Interface (GUI).
    * Uses static exchange rates (you can extend this to integrate with a real-time API).

* **Expense Tracker:**
    * Allows adding, viewing, and tracking expenses via a Command-Line Interface (CLI).
    * Securely stores your expense data in an `expenses.csv` file (or `expenses.json` if configured).
    * Ability to plot visual representations (pie charts and bar charts) of your expenses.

---

## Requirements

To successfully run this project on your computer, you will need Python 3.x and a few essential Python libraries.

1.  **Python 3.x:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).
2.  **Required Python Libraries:** You'll need to install `requests` (if you plan to use a currency API) and `matplotlib` (for plotting expenses).
    Install them by running this command in your Command Prompt (or VS Code's integrated terminal):
    ```bash
    pip install requests matplotlib
    ```

---

## How to Run

Follow these steps to download and run the project on your computer:

1.  **Download the Project:**
    * Go to this GitHub repository page.
    * Click the **`<> Code`** button (it's usually green).
    * Select **"Download ZIP"**.
    * Once downloaded, unzip the file into a folder on your computer (e.g., `Python-Finance-Tools-main`).

2.  **Open Command Prompt/Terminal:**
    * Open the folder where you unzipped the project (e.g., `Python-Finance-Tools-main`) in your File Explorer.
    * Click on the address bar at the top of the folder (where the folder path is displayed).
    * Type **`cmd`** and press **Enter**. A Command Prompt window will open directly in that folder.

3.  **Run the Programs:**
    From the Command Prompt, you can run different programs using these commands:

    * **Currency Converter (CLI):**
        ```bash
        python cli_converter.py
        ```
        *Input example: amount (e.g., `100`), source currency code (e.g., `USD`), target currency code (e.g., `INR`)*

    * **Currency Converter (GUI):**
        ```bash
        python gui_converter.py
        ```
        *This will open a new GUI window for interaction.*

    * **Expense Tracker (CLI):**
        ```bash
        python cli_expense_tracker.py
        ```
        *This will display a menu where you can add, view, and plot expenses.*

---

## File Structure

The project folder structure is as follows:

Python-Finance-Tools-main/
├── currency_converter.py      # Core currency conversion logic
├── cli_converter.py           # Command-Line Interface for Currency Converter
├── gui_converter.py           # Graphical User Interface for Currency Converter
├── expense_tracker.py         # Core expense tracking logic
├── cli_expense_tracker.py     # Command-Line Interface for Expense Tracker
└── README.md                  # This file
└── expenses.csv               # Created when you add data to the Expense Tracker (or .json optionally)
