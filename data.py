from typing import List, Dict, Any
import random
from datetime import datetime, timedelta

# Dữ liệu giả cho users
fake_users = [
    {
        "id": 1,
        "name": "Nguyễn Văn An",
        "email": "an.nguyen@example.com",
        "age": 25,
        "city": "Hà Nội",
        "created_at": "2024-01-15T10:30:00Z"
    },
    {
        "id": 2,
        "name": "Trần Thị Bình",
        "email": "binh.tran@example.com",
        "age": 30,
        "city": "TP. Hồ Chí Minh",
        "created_at": "2024-01-20T14:15:00Z"
    },
    {
        "id": 3,
        "name": "Lê Văn Cường",
        "email": "cuong.le@example.com",
        "age": 28,
        "city": "Đà Nẵng",
        "created_at": "2024-02-01T09:45:00Z"
    },
    {
        "id": 4,
        "name": "Phạm Thị Dung",
        "email": "dung.pham@example.com",
        "age": 35,
        "city": "Hải Phòng",
        "created_at": "2024-02-10T16:20:00Z"
    },
    {
        "id": 5,
        "name": "Hoàng Văn Em",
        "email": "em.hoang@example.com",
        "age": 22,
        "city": "Cần Thơ",
        "created_at": "2024-02-15T11:10:00Z"
    }
]

# Dữ liệu giả cho products
fake_products = [
    {
        "id": 1,
        "name": "iPhone 15 Pro",
        "price": 29990000,
        "category": "Điện thoại",
        "brand": "Apple",
        "stock": 50,
        "description": "iPhone 15 Pro với chip A17 Pro mạnh mẽ"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 24990000,
        "category": "Điện thoại",
        "brand": "Samsung",
        "stock": 30,
        "description": "Galaxy S24 với camera AI tiên tiến"
    },
    {
        "id": 3,
        "name": "MacBook Air M2",
        "price": 25990000,
        "category": "Laptop",
        "brand": "Apple",
        "stock": 25,
        "description": "MacBook Air với chip M2 hiệu năng cao"
    },
    {
        "id": 4,
        "name": "Dell XPS 13",
        "price": 22990000,
        "category": "Laptop",
        "brand": "Dell",
        "stock": 20,
        "description": "Dell XPS 13 với thiết kế sang trọng"
    },
    {
        "id": 5,
        "name": "AirPods Pro 2",
        "price": 5990000,
        "category": "Phụ kiện",
        "brand": "Apple",
        "stock": 100,
        "description": "AirPods Pro thế hệ 2 với chống ồn chủ động"
    }
]

# Dữ liệu giả cho posts
fake_posts = [
    {
        "id": 1,
        "title": "Hướng dẫn lập trình Python cơ bản",
        "content": "Python là một ngôn ngữ lập trình mạnh mẽ và dễ học...",
        "author": "Nguyễn Văn An",
        "category": "Lập trình",
        "likes": 45,
        "created_at": "2024-01-10T08:00:00Z"
    },
    {
        "id": 2,
        "title": "Công nghệ AI và tương lai",
        "content": "Trí tuệ nhân tạo đang thay đổi cách chúng ta sống và làm việc...",
        "author": "Trần Thị Bình",
        "category": "Công nghệ",
        "likes": 78,
        "created_at": "2024-01-12T14:30:00Z"
    },
    {
        "id": 3,
        "title": "Review iPhone 15 Pro",
        "content": "Sau 1 tuần sử dụng iPhone 15 Pro, đây là những trải nghiệm của tôi...",
        "author": "Lê Văn Cường",
        "category": "Review",
        "likes": 92,
        "created_at": "2024-01-15T10:15:00Z"
    }
]

def get_random_user() -> Dict[str, Any]:
    """Trả về một user ngẫu nhiên"""
    return random.choice(fake_users)

def get_random_product() -> Dict[str, Any]:
    """Trả về một sản phẩm ngẫu nhiên"""
    return random.choice(fake_products)

def get_random_post() -> Dict[str, Any]:
    """Trả về một bài viết ngẫu nhiên"""
    return random.choice(fake_posts)

def generate_random_data(data_type: str, count: int = 1) -> List[Dict[str, Any]]:
    """Tạo dữ liệu ngẫu nhiên theo loại và số lượng"""
    if data_type == "user":
        return random.sample(fake_users, min(count, len(fake_users)))
    elif data_type == "product":
        return random.sample(fake_products, min(count, len(fake_products)))
    elif data_type == "post":
        return random.sample(fake_posts, min(count, len(fake_posts)))
    else:
        return []
