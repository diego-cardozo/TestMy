# Diego Cardozo
## Just a simple example based en Behave

Scenario: Open Google web page and make a search by clicking in "I'm Feeling Lucky" Button
    Given I open "http://www.google.com"
    When I create search "Diego Cardozo - Senior Software Development Engineer in Test"
    Then I click in Iam Feeling Lucky button


### How to set up the Test Framework environment

#### Installed Prerequisites:
* Firefox: 57.0 or greater
* Python: 3.6.1 or greater

#### Setup
* Open a Commandline console with Administrator rights
* Run install_deps.bat

### How to run the test
Just as simple to execute:
* run_test.bat

### What I should expect if everything is ok?

#### You will see this output:

C:\repos\TestMy>run_test.bat
"****************************************************"
"* Running TestMy..."
"****************************************************"
Feature: Simple browser testing # features/feature_files/testmy.feature:1
  """
  A simple example
  """
  Scenario: Open Google web page and make a search by clicking in "I'm Feeling Lucky" Button  # features/feature_files/testmy.fea
ture:8
    Given I open "http://www.google.com"                                                      # features/steps/test_my.py:7
    When I create search "Diego Cardozo - Senior Software Development Engineer in Test"       # features/steps/test_my.py:13
    Then I click in Iam Feeling Lucky button                                                  # features/steps/test_my.py:18

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.477s
"****************************************************"
"* Done"
"****************************************************"