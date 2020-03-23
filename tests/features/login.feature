Feature: Login service

    Scenario Outline: status codes
        Given I fill form field login with <login>
        And I fill form field password with <password>
        When I try to log in
        Then it should return <status_code>


     Examples:
       | login  | password  | status_code   |
       | foo    | bar       | 200           |
       | john   | invalid   | 401           |
