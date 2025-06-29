from fastapi import APIRouter
from .products.view import router as products_router

router = APIRouter()
router.include_router(products_router, prefix="/products", tags=["Products"])