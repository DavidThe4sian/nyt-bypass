from flask import Flask
from nytRecipe.__init__ import create_app

application = create_app()

if __name__ == "__main__":
    application.run()
