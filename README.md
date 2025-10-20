# Demo API với dữ liệu giả

Đây là một API đơn giản được xây dựng bằng Python FastAPI, cung cấp dữ liệu giả cho việc testing và phát triển.

## Tính năng

- ✅ API RESTful với FastAPI
- ✅ Dữ liệu giả cho Users, Products, Posts
- ✅ Các endpoint với query parameters
- ✅ Tự động tạo documentation (Swagger UI)
- ✅ CORS enabled cho frontend
- ✅ Error handling

## Cài đặt

1. **Clone hoặc tải project về máy**

2. **Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

3. **Chạy server:**
```bash
python main.py
```

Hoặc sử dụng uvicorn trực tiếp:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. **Truy cập API:**
- API Base URL: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### 🏠 Root
- `GET /` - Thông tin API và danh sách endpoints

### 👥 Users
- `GET /users` - Lấy danh sách users
  - Query params: `limit`, `random`
- `GET /users/{user_id}` - Lấy user theo ID

### 🛍️ Products  
- `GET /products` - Lấy danh sách products
  - Query params: `limit`, `random`, `category`
- `GET /products/{product_id}` - Lấy product theo ID

### 📝 Posts
- `GET /posts` - Lấy danh sách posts
  - Query params: `limit`, `random`, `category`
- `GET /posts/{post_id}` - Lấy post theo ID

### 🎲 Random Data
- `GET /random/{data_type}` - Lấy dữ liệu ngẫu nhiên
  - `data_type`: `user`, `product`, `post`
  - Query param: `count` (1-10)

### 📊 Statistics
- `GET /stats` - Thống kê tổng quan
- `GET /health` - Health check

## Ví dụ sử dụng

### Lấy tất cả users:
```bash
curl http://localhost:8000/users
```

### Lấy 3 users ngẫu nhiên:
```bash
curl "http://localhost:8000/users?limit=3&random=true"
```

### Lấy products theo category:
```bash
curl "http://localhost:8000/products?category=Điện thoại"
```

### Lấy 5 posts ngẫu nhiên:
```bash
curl "http://localhost:8000/random/post?count=5"
```

### Lấy user theo ID:
```bash
curl http://localhost:8000/users/1
```

## Cấu trúc dữ liệu

### User
```json
{
  "id": 1,
  "name": "Nguyễn Văn An",
  "email": "an.nguyen@example.com",
  "age": 25,
  "city": "Hà Nội",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Product
```json
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "price": 29990000,
  "category": "Điện thoại",
  "brand": "Apple",
  "stock": 50,
  "description": "iPhone 15 Pro với chip A17 Pro mạnh mẽ"
}
```

### Post
```json
{
  "id": 1,
  "title": "Hướng dẫn lập trình Python cơ bản",
  "content": "Python là một ngôn ngữ lập trình mạnh mẽ và dễ học...",
  "author": "Nguyễn Văn An",
  "category": "Lập trình",
  "likes": 45,
  "created_at": "2024-01-10T08:00:00Z"
}
```

## Mở rộng

Bạn có thể dễ dàng mở rộng API này bằng cách:

1. **Thêm dữ liệu mới** trong file `data.py`
2. **Tạo endpoints mới** trong file `main.py`
3. **Thêm validation** với Pydantic models
4. **Kết nối database** thực (SQLite, PostgreSQL, MongoDB...)
5. **Thêm authentication** và authorization

## Công nghệ sử dụng

- **FastAPI**: Web framework hiện đại cho Python
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Python 3.7+**

## License

MIT License - Sử dụng tự do cho mục đích học tập và phát triển.
