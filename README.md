# PyDriverFramework
[Python](https://www.python.org/) wrapper framework for
[Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/) using the
[Page Object Model](https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#page-object-design-pattern).
> Note: The documentation in this project assumes the reader has prior knowledge and experience using a CLI, Python,
  Selenium WebDriver, and writing tests using the Python bindings for Selenium WebDriver explicitly (without using
  Selenium IDE). If the reader doesn't have knowledge of these topics, it is strongly recommended that the reader gain
  knowledge of them prior to reading this documentation and using this project.

[![Build Status](https://jenkins.mwaltman.com/buildStatus/icon?job=PyWebDriverFramework/master)](https://jenkins.mwaltman.com:8443/job/PyWebDriverFramework/job/master/)

## Objective
The objective of this project is to create an abstraction layer between Selenium WebDriver and tests written in Python
that use WebDriver. This project aims to create a simple, lightweight API that includes:
- a basic structure for a Page Object Model to build off of
- keeping WebDriver methods out of tests
- mitigating test errors and false negatives that can occur when Selenium loses track of web elements
- a structure for storing test data for the purpose of keeping page objects stateless

## Prerequisites
This project requires the following:
- Linux, MacOS, or Windows machine with Python 3.6+, pip, and pytest3 installed.
- Browsers you will test against installed on the machine you will test against. Note that if you are using remote
  WebDriver, the browser(s) must be installed on the remote machine you will be testing against.
- A driver for each of the platform(s) and browser(s) you will test against, each of which can be found on the pages
  linked below. Make sure that the driver you download supports the browser version(s) you will be testing against. You
  may need multiple drivers if you want to test older versions of the same browser. Note that if you are using remote
  WebDriver, the driver(s) must be installed on the machine you will run the tests on, not the machine you are testing
  against.
    + [Google Chrome (chromedriver)](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    + [Firefox (geckodriver)](https://github.com/mozilla/geckodriver/releases)
    + [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
    + [Internet Explorer](http://selenium-release.storage.googleapis.com/index.html?path=3.6/)
    + [Opera (operachromiumdriver)](https://github.com/operasoftware/operachromiumdriver/releases)
    + Safari: SafariDriver is included with Safari as of Safari 10, to enable it:
        1. Open Safari and open the Safari menu and click "Preferences"
        2. Navigate to the "Advanced" tab
        3. At the bottom of the window, check "Show Develop menu in menu bar"
        4. Open the "Develop" menu and click "Allow Remote Automation" near the bottom
        5. Open your preferred CLI and enter `safaridriver --enable`
        6. Enter your password
        7. SafariDriver is now fully enabled
    + [SafariDriver Extension](http://selenium-release.storage.googleapis.com/2.48/SafariDriver.safariextz): Download
      SafariDriver for Safari under version 10. This is deprecated and should only be used if you specifically
      require testing Safari versions under 10.
    + [GhostDriver](https://github.com/detro/ghostdriver) for testing with [PhantomJS](http://phantomjs.org/) (a
      headless browser)
    + [HtmlUnitDriver](https://github.com/seleniumhq/htmlunit-driver) for testing with
      [HtmlUnit](http://htmlunit.sourceforge.net/) (another headless browser)
- If you are using remote WebDriver, an additional Linux, MacOS, or Windows server running a WebDriver server that you
  will test against.

## Project Structure
##### Jenkinsfile
Build pipeline specification for Jenkins to use when building this project.
##### requirements.txt
Python package dependencies that this project uses.
##### setup.py
Project setup script.
##### wdframework/
Source code for this project.

## Download
To download and start using this project you can do any of the following:
- Download a [release](https://github.com/dubszy/PyWebDriverFramework/releases)
- Download a specific branch as a ZIP by selecting the branch to download from the "Branch" dropdown menu, then using
  the "Clone or download" dropdown menu and clicking "Download ZIP"
- Include it as a submodule in your repo by running `git submodule add git@github.com:dubszy/PyWebDriverFramework.git`
- Clone it by running `git clone git@github.com:dubszy/PyWebDriverFramework.git`

## Setup
At this point, you should have Python 3.6+, pip, and pytest3 installed.
- Install dependencies: `pip install -r requirements.txt`
- Optionally run the included tests: `py.test3 tests`

## Installation
WIP

## Usage
WIP

## Contributing
Contributions to this project are always welcome and can be made forking it and filing a
[pull request](https://github.com/dubszy/PyWebDriverFramework/compare). In your PR, please include a clear description
of the nature (feature addition, bug fix, etc) of your contribution.
