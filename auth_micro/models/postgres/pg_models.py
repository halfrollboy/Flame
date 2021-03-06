from email.policy import default
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from ...db.postgres.database import Model


class User(Model):
   __tablename__ = 'user'
   id = Column(Integer, primary_key=True)
   username = Column(String)
   fullname = Column(String)
   password = Column(String)
   email = Column(String, unique=True, index=True)
   phone = Column(String, unique=True, default=None)

   def __repr__(self):
      return "<User(name='%s', fullname='%s', password='%s')>" % (
                           self.name, self.fullname)


class Company(Model):
   __tablename__ = "company"

   id = Column(Integer(), primary_key=True)
   name = Column(String)
   phone = Column(String, unique=True)
   email = Column(String, unique=True, index=True)
   adress = Column(String)
   coordinate = Column(String)
   info_id = Column(Integer)
   edited = Column(Boolean, nullable=False, default=True)


class Employee(Model):
   __tablename__ = "employee"

   id = Column(Integer, primary_key=True)
   name = Column(String(200), nullable=False)
   fio = Column(String(200))
   phone = Column(String, unique=True)
   company_id = Column(Integer, ForeignKey('company.id'))
   email = Column(String, unique=True, index=True, nullable=False)
   password = Column(String, nullable=False)
   gender = Column(Boolean, nullable=False)
   info = Column(Integer)
   admin = Column(Boolean, nullable=False)
   owner = Column(Boolean, nullable=False)