## Migration commands

Create the migrations folder once the database connections are configured in app:
```sh
flask db init
```

Create a migration:
```sh
flask db migrate -m "your migration message"
```

Apply migration to database:
```sh
flask db upgrade
```

## SQLAlchemy queries

### Select statements

Get all of an entity:
```py
>>> from app.models import User
>>> User.query.all()
```

Create new entity:
```py
>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```

Get a single entity by ID:
```py
>>> u = User.query.get(1)
```

Get a single entity by a filter:
```py
>>> User.query.filter_by(username='user123').first()
```
