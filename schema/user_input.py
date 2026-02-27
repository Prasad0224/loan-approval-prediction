from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal

class LoanApplicant(BaseModel):

    person_income: Annotated[
        float,
        Field(..., description="Annual income (INR)", gt=10000, example=55000)
    ]

    loan_amnt: Annotated[
        float,
        Field(..., description="Requested loan amount", gt=0, example=15000)
    ]

    loan_int_rate: Annotated[
        float,
        Field(..., description="Interest rate (%)", gt=0, example=13.5)
    ]

    cb_person_cred_hist_length: Annotated[
        int,
        Field(..., description="Credit history length (years)", ge=0, example=6)
    ]

    person_emp_length: Annotated[
        float,
        Field(..., description="Employment length (years)", ge=0, example=4.5)
    ]

    person_age: Annotated[
        int,
        Field(..., description="Applicant age", ge=18, le=60, example=29)
    ]

    cb_person_default_on_file: Annotated[
        Literal["Y", "N"],
        Field(..., description="Previous default on record")
    ]

    loan_grade: Annotated[
        Literal["A", "B", "C", "D", "E", "F", "G"],
        Field(..., description="Loan grade assigned by lender")
    ]

    person_home_ownership: Annotated[
        Literal["RENT", "OWN", "MORTGAGE", "OTHER"],
        Field(..., description="Home ownership status")
    ]

    loan_intent: Annotated[
        Literal[
            "PERSONAL",
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "HOMEIMPROVEMENT",
            "DEBTCONSOLIDATION"
        ],
        Field(..., description="Purpose of the loan")
    ]


    @field_validator("cb_person_default_on_file")
    @classmethod
    def default_uppercase(cls, value: str) -> str:

        return value.upper()


    @computed_field
    @property
    def loan_percent_income(self) -> float:

        return round(self.loan_amnt / self.person_income, 4)
        