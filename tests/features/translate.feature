Feature: Translate response to the client prefered language

    Scenario Outline: Invalid login
        Given accept language header <language>
        When I failed to log in
        Then I should get status response <response>

    Examples:
        | language  | response              |
        | en        | Login failed          |
        | pl        | Nieudane logowanie    |

    Scenario Outline: Login successul
        Given accept language header <language>
        When I log in
        Then I should get status response <response>

    Examples:
        | language  | response              |
        | en        | Login Successful      |
        | pl        | Pomyślnie zalogowano  |
