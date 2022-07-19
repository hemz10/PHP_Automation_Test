
# PHP Travels - Test Automation

Python - Selenium - Pytest

This repository contains Automated Web UI Tests for PHP Travel website. The tests have been implemented using Python, Selenium, and Pytest. The test scenarios covered are:

1> Signing In 

2> Checking for Hotel by Entering City, Checkin and Checkout date, travellers count.

3> Entering From and To destination for a round trip and checking for flights for a particular date
Total Tests: 2

# Environment Setup

1> Download and install Python 3 from [here](https://www.python.org/downloads/). For Windows users, make sure to check the 'Add Python to Path' box during the setup.

2> Download the repository files.

3>Open a terminal/Command Prompt and cd into 'PHP_Automation_Test' directory:
```bash
cd path-to-Conduit_Test_Project-directory
```

4> Run the command (requires administrator/root privileges and an internet connection):
Windows Users should run command prompt as Administrator and enter:
``` bash
pip3 install -r requirements.txt
```
Linux/Mac users should enter:
```bash
sudo pip3 install -r requirements.txt
```
## Running Tests

1> Open a terminal/Command Prompt and cd into the Conduit_Test_Project directory.

2> To run all the tests, execute the command
```bash
pytest 
```
Note: Sometimes you might face server issue, when you face this issue please try after sometime.

3> To generate an HTML report, use the switch, --html:
```bash
pytest --html=report.html
```


## Test Artifacts

Everytime test(s) are executed using the pytest command, a separate folder bearing a timestamp is created for that test-run inside Report\ directory. All the logs generated during the test-run can be found in this directory.we can also add html report during runtime in the same directory using the command:
``` bash
pytest --html= 'path to report directory'/report.html
```

## Framework Features

* Modular

    * Web Pages have been represented through a Page Object Model (POM).
    * No webdriver api in actual tests. Tests are created by only using aptly named functions. API is restricted to pages and elements classes.
    * Intuitive folder structure that keeps various aspects of the framework organized

* Reporting

    * A separate folder with timestamp is created for each test run containing logs, screenshots and an HTML report.
    * An HTML report can easily be generated that summarises passes, failures, logs, time taken by each test etc.


## 🛠 Skills
Python, Pytest, Selenium...

# Thank You

