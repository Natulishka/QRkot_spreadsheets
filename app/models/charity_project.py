from sqlalchemy import Column, String, Text

from app.models.base import ProjectsAndDonationBase


class CharityProject(ProjectsAndDonationBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Целевой проект {self.name} на сумму {self.full_amount}'
        )
