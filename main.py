from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
import random
from data import (
    fake_users, 
    fake_products, 
    fake_posts,
    get_random_user,
    get_random_product,
    get_random_post,
    generate_random_data
)

# Khởi tạo FastAPI app
app = FastAPI(
    title="Demo API với dữ liệu giả",
    description="API đơn giản trả về dữ liệu giả cho testing",
    version="1.0.0"
)

# Cấu hình CORS để cho phép frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Chào mừng đến với Demo API!",
        "version": "1.0.0",
        "endpoints": {
            "users": "/users",
            "products": "/products", 
            "posts": "/posts",
            "random": "/random/{type}",
            "docs": "/docs"
        }
    }

# API endpoints cho Users
@app.get("/users", response_model=List[Dict[str, Any]])
async def get_users(
    limit: Optional[int] = Query(None, description="Số lượng users muốn lấy"),
    random: bool = Query(False, description="Lấy users ngẫu nhiên")
):
    """Lấy danh sách users"""
    if random:
        if limit:
            return generate_random_data("user", limit)
        return [get_random_user()]
    
    if limit:
        return fake_users[:limit]
    return fake_users

@app.get("/users/{user_id}", response_model=Dict[str, Any])
async def get_user_by_id(user_id: int):
    """Lấy user theo ID"""
    user = next((user for user in fake_users if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User không tồn tại")
    return user

# API endpoints cho Products
@app.get("/products", response_model=List[Dict[str, Any]])
async def get_products(
    limit: Optional[int] = Query(None, description="Số lượng products muốn lấy"),
    random: bool = Query(False, description="Lấy products ngẫu nhiên"),
    category: Optional[str] = Query(None, description="Lọc theo category")
):
    """Lấy danh sách products"""
    products = fake_products.copy()
    
    # Lọc theo category nếu có
    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]
    
    if random:
        if limit:
            return generate_random_data("product", limit)
        return [get_random_product()]
    
    if limit:
        return products[:limit]
    return products

@app.get("/products/{product_id}", response_model=Dict[str, Any])
async def get_product_by_id(product_id: int):
    """Lấy product theo ID"""
    product = next((product for product in fake_products if product["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product không tồn tại")
    return product

# API endpoints cho Posts
@app.get("/posts", response_model=List[Dict[str, Any]])
async def get_posts(
    limit: Optional[int] = Query(None, description="Số lượng posts muốn lấy"),
    random: bool = Query(False, description="Lấy posts ngẫu nhiên"),
    category: Optional[str] = Query(None, description="Lọc theo category")
):
    """Lấy danh sách posts"""
    posts = fake_posts.copy()
    
    # Lọc theo category nếu có
    if category:
        posts = [p for p in posts if p["category"].lower() == category.lower()]
    
    if random:
        if limit:
            return generate_random_data("post", limit)
        return [get_random_post()]
    
    if limit:
        return posts[:limit]
    return posts

@app.get("/posts/{post_id}", response_model=Dict[str, Any])
async def get_post_by_id(post_id: int):
    """Lấy post theo ID"""
    post = next((post for post in fake_posts if post["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post không tồn tại")
    return post

# API endpoint cho random data
@app.get("/random/{data_type}", response_model=List[Dict[str, Any]])
async def get_random_data(
    data_type: str,
    count: int = Query(1, ge=1, le=10, description="Số lượng items muốn lấy (1-10)")
):
    """Lấy dữ liệu ngẫu nhiên theo loại"""
    valid_types = ["user", "product", "post"]
    if data_type not in valid_types:
        raise HTTPException(
            status_code=400, 
            detail=f"Loại dữ liệu không hợp lệ. Chọn một trong: {', '.join(valid_types)}"
        )
    
    return generate_random_data(data_type, count)

# API endpoint để lấy thống kê
@app.get("/stats")
async def get_stats():
    """Lấy thống kê tổng quan"""
    return {
        "total_users": len(fake_users),
        "total_products": len(fake_products),
        "total_posts": len(fake_posts),
        "categories": {
            "products": list(set(p["category"] for p in fake_products)),
            "posts": list(set(p["category"] for p in fake_posts))
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Kiểm tra trạng thái API"""
    return {"status": "healthy", "message": "API đang hoạt động bình thường"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
