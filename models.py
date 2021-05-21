from sqlalchemy import MetaData, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Job(Base):
    __tablename__ = "job"
    id = Column(String(36), primary_key=True)
    title = Column(String(50), nullable=False)
    salary = Column(Integer, nullable=True)
    start_date = Column(Date, nullable=True)
    location = Column(String(100), nullable=False)
    company = Column(String(50), nullable=False)
    sector = Column(String(50), nullable=True)
    description = Column(String(500), nullable=True)
    created = Column(DateTime, default=datetime.utcnow())
    users = relationship("User", secondary="application", back_populates="jobs")


class User(Base):
    __tablename__ = "user"
    id = Column(String(36), primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=True)
    created = Column(DateTime, default=datetime.utcnow())
    jobs = relationship("Job", secondary="application", back_populates="users")


class Application(Base):
    __tablename__ = "application"
    user_id = Column(String(36), ForeignKey("user.id"), primary_key=True)
    job_id = Column(String(36), ForeignKey("job.id"), primary_key=True)
    status = Column(String(10), default=0)
    message = Column(String(500), nullable=True)
    created = Column(DateTime, default=datetime.utcnow())


class Employer(Base):
    __tablename__ = "employer"
    id = Column(String(36), primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.utcnow())