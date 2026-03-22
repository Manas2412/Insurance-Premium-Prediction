from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities



#pydantic model to validate incoming data
class User(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="The age of the user", example=30)]
    weight: Annotated[float, Field(..., gt=0, description="The weight of the user in kg", example=70.0)]
    height: Annotated[float, Field(..., gt=0, description="The height of the user in cm", example=175.5)]
    income_lpa: Annotated[int, Field(..., description="The income of the user", example=100)]
    smoker: Annotated[bool, Field(..., description="The smoker status of the user", example=True)]
    city: Annotated[ str, Field(..., description="The city of the user", example="New York")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        v = v.strip().title()
        return v

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        