from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contract(Base):

    __tablename__ = "contracts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    borrower_name = Column(String)

    lender_name = Column(String)

    loan_amount = Column(Float)

    interest_rate = Column(Float)

    emi_amount = Column(Float)

    loan_duration_months = Column(Integer)

    processing_fee = Column(Float)

    penalty_charges = Column(String)

    interest_type = Column(String)

    foreclosure_charges = Column(String)

    late_payment_fee = Column(String)