Feature: Test

  @web-au
  Scenario: Country flag order
    Given user is on "AU" research landing page
    When user search by term "crime" in BRSB
    Then user is on search result page for "crime"
    And the "1st" country flag is "AU"
    And the "2nd" country flag is "UK"
    And the other country flags are sort alphabetically

#  Scenario: HLCT
#    Given user is on "AU" research landing page
#    When user search by term "crime" in BRSB
#    Then user is on search result page for "crime"
#    And the following HLCT are displayed
#
#    | Order | HLCT |
#    | 1     | AU Cases |
#    | 2     | AU Legislation |
#    | 3     | AU Analytical Materials |
#    | 4     | AU Forms & Precedents   |
