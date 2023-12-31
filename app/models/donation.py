from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import ProjectsAndDonationBase


class Donation(ProjectsAndDonationBase):
    user_id = Column(Integer, ForeignKey('user.id',
                                         name='fk_donation_user_id_user'))
    comment = Column(Text)

    def __repr__(self):
        return (
            f'Пожертвование на сумму {self.full_amount}'
        )