from datetime import timedelta
from typing import Dict, List, Optional, Union

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict[str, Union[str, timedelta]]]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested).order_by(
                    desc(func.julianday(CharityProject.close_date) -
                         func.julianday(CharityProject.create_date)))
        )
        projects = projects.scalars().all()
        report_projects = []
        for project in projects:
            report_projects.append({
                'name': project.name,
                'donations time': str(project.close_date - project.create_date),
                'description': project.description,
            })
        return report_projects


charity_project_crud = CRUDCharityProject(CharityProject)
