from memory.schemas import (
    Base,
    engine,
    SessionLocal,
    Doctor
)


Base.metadata.create_all(bind=engine)

db = SessionLocal()

doctors = [
    Doctor(
        name="Dr Sharma",
        specialization="Cardiologist"
    ),
    Doctor(
        name="Dr Priya",
        specialization="Dermatologist"
    ),
    Doctor(
        name="Dr Kumar",
        specialization="Neurologist"
    )
]

for doctor in doctors:

    exists = db.query(Doctor).filter(
        Doctor.name == doctor.name
    ).first()

    if not exists:
        db.add(doctor)

db.commit()

print("Database seeded")