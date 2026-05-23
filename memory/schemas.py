from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from config import DB_URL


Base = declarative_base()

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Patient(Base):

    __tablename__ = "patients"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    preferred_language = Column(String)


class Doctor(Base):

    __tablename__ = "doctors"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    specialization = Column(String)


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_name = Column(String)

    doctor_name = Column(String)

    slot = Column(String)

    status = Column(String)