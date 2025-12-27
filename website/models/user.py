from flask_login import UserMixin

class User(UserMixin):
        def __init__(self, doc):
            self.doc = doc or {}
            self.id = str(self.doc.get("_id"))

        @property 
        def is_active(self):
            return bool(self.doc.get("is_active", True))
        
        @property
        def is_anonymous(self) -> bool:
            return False
        
        @property
        def is_authenticated(self) -> bool:
            return True
        
        @property
        def is_admin(self):
            return self.doc.get("role") == "admin"
        
        @property
        def role(self):
            return self.doc.get("role", "user")
        
        @property
        def email(self):
            return self.doc.get("email")
        
        @property
        def username(self):
            return self.doc.get("username")

        def get_id(self) -> str:
            return self.id