"""
Script to run the main application.

This script imports the 'app' object from the 'main' module and checks if it is
being run as the main program. If so, it invokes the 'run' method of the 'app'
object to start the application.
"""
from app.main import app

if __name__ == "__main__":
    app.run()
