Feature: Simple browser testing
"""
A simple example

"""

Scenario: Open Google web page and make a search by clicking in "I'm Feeling Lucky" Button
    Given I open "http://www.google.com"
    When I create search "Diego Cardozo - Senior Software Development Engineer in Test"
    Then I click in Iam Feeling Lucky button
