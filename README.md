# Automated Clinical Report Generator

This application is designed to generate clinical reports in PDF format. The reports are generated automatically based on the input data provided in formats like .json, .csv, .txt. Each report is generated according to a standardized template, with the only differences being the input data (the clinical information of different customers).

## Setup and Installation

1. Clone this repo to your local machine.

2. Install the required Python libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

Usage:
```bash
python main.py
```

---

## Dependencies

This program depends on WeasyPrint, which in turn depends on GTK. This section explains how to install GTK on different platforms.

### Windows

1. Download and install [MSYS2](https://www.msys2.org/).

2. Open the MSYS2 terminal (either MSYS2 MinGW 64-bit or MSYS2 MinGW 32-bit, depending on whether your system is 64-bit or 32-bit).

3. Update the package database and core system packages with:

    ```bash
    pacman -Syu
    ```

4. If needed, close the MSYS2 terminal and reopen it to continue with the update.

5. Install GTK with:

    ```bash
    pacman -S mingw-w64-x86_64-gtk3
    ```

    For 32-bit systems, use:

    ```bash
    pacman -S mingw-w64-i686-gtk3
    ```

6. Add the GTK bin directory to your system's PATH. For 64-bit systems, this is typically `C:\msys64\mingw64\bin`. For 32-bit systems, it's typically `C:\msys64\mingw32\bin`.

7. Restart your computer.

### MacOS

1. If you do not have Homebrew installed, install it by following instructions at [https://brew.sh/](https://brew.sh/).

2. Install GTK with the following command:

    ```bash
    brew install gtk+3
    ```

### Linux (Ubuntu)

1. Install the necessary packages with the following command:

    ```bash
    sudo apt-get install libgirepository1.0-dev gobject-introspection gir1.2-gtk-3.0
    ```

---

https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows
    