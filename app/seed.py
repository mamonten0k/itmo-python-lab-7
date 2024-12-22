from sqlalchemy.orm import Session
from app import models

DEFAULT_TERMS = [
    {
        "name": "Widget",
        "description": "Flutter is completely all about widgets. A widget is used to make the user interface(UI) in the flutter application. To make beautiful UI in flutter we have good knowledge about different widgets. A widget can Color, Text, Button, ListView, AppBar, etc.",
    },
    {
        "name": "StatelessWidget",
        "description": "In our user interface(UI), some common widgets such as page title name, the background color of a screen, a title, or a static image. These widgets do not need to change dynamically so these widgets can be defined inside the class that extends stateless widgets.",
    },
    {
        "name": "StatefulWidget",
        "description": "In Flutter, a Stateful widget is a type of widget that can dynamically change its appearance in response to user interactions. Unlike a StatelessWidget, which is immutable and cannot change its appearance. When you use a Stateful widget, you need to manage the state of the widget yourself.",
    },
    {
        "name": "State",
        "description": "The state is information that can change within an app and affects the user interface. The state is managed by widgets. A widget can either be stateful or stateless.",
    },
    {
        "name": "Pub",
        "description": "Pub is Package Manager which is used to manage dependencies for Flutter projects, allowing developers to easily include external libraries and packages in their projects. With Pub, you can search for packages, download packages, and manage the version of packages that you use in your projects.",
    },
]

def seed_database(db: Session):
    for term in DEFAULT_TERMS:
        existing_term = db.query(models.Term).filter(models.Term.name == term["name"]).first()
        if not existing_term:
            new_term = models.Term(name=term["name"], description=term["description"])
            db.add(new_term)
    db.commit()
