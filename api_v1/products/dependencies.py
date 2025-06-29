from typing import Annotated

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_healper, Product


async def product_by_id(
        product_id: Annotated[int, Path], 
        session=Depends(db_healper.scoped_session_dependency)
) -> Product:
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
)