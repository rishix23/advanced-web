"""
models.py

Creates and defines models used throughout the application. This needs to be shared by
a number of different services. ONLY EDIT THIS FILE AT THE APPLICATION ROOT, NOT IN AN
INDIVIDUAL SERVICE. This file is copied from the root into individual services at build.
"""

from sqlalchemy import MetaData, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import LargeBinary

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Job(Base):
    __tablename__ = "job"
    id = Column(String(36), primary_key=True)
    employer_id = Column(String(36), ForeignKey("employer.id"))
    title = Column(String(50), nullable=False)
    salary = Column(Integer, nullable=True)
    start_date = Column(Date, nullable=True)
    location = Column(String(100), nullable=False)
    company = Column(String(50), nullable=False)
    sector = Column(String(50), nullable=True)
    description = Column(String(500), nullable=True)
    created = Column(DateTime, default=datetime.utcnow())


class Application(Base):
    __tablename__ = "application"
    id = Column(String(36), primary_key=True)
    job_id = Column(String(36), ForeignKey("job.id"))
    full_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(60), nullable=False)
    resume = Column(LargeBinary, nullable=False)
    created = Column(DateTime, default=datetime.utcnow())


class Employer(Base):
    __tablename__ = "employer"
    id = Column(String(36), primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(60), nullable=False)
    jobs = relationship("Job")
    created = Column(DateTime, default=datetime.utcnow())