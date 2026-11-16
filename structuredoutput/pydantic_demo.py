from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Unknown"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lte=10, default = 5.0, description="CGPA must be between 0 and 10")

new_student = {'name': 'John Doe','age':28,'email':'john@example.com','cgpa':10}
student = Student(**new_student)

print(student)  