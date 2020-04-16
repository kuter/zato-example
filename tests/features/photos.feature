Feature: Photos service

    Scenario Outline: Resources should be accesible only for logged users
        When I try to see a photo <photo_id>
        Then it should return <status_code>

    Examples:
        | photo_id  | status_code   |
        | 1         | 200           |
        | 2         | 403           |
        | 123       | 404           |

    Scenario: User with permission can view photo
        Given I logged in
        When I try to see a photo 2
        Then it should return 200
