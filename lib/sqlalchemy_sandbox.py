#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    students = [
        "Ross Geller",
        "Chandler Bing",
        "Monica Geller",
        "Joey Tribbiani",
        "Phoebe Buffay",
        "Rachel Green"
    ]
    for name in students:
        existing = session.query(Student).filter_by(name=name).first()
        if not existing:
            student = Student(name=name)
            session.add(student)
            print(f"Added student: {student.name}")
        else:
            print(f"Student already exists: {existing.name}")

    session.commit()


    all_students = session.query(Student).all()
    for student in all_students:
        print(f"ID: {student.id}, Name: {student.name}")
