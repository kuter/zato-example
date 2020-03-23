Feature: tests built-in zato.ping service

    Scenario: run a simple test
        Given built-in ping service
        When we call ping service
        Then response should be ok
