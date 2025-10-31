# Leer el contenido actual de main.py
with open('main.py', 'r') as f:
    content = f.read()

# Reemplazar la parte problemática de get_posts
old_get_posts = '''@app.get("/api/posts", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    
    # Add info if it's from current user (mock)
    for post in posts:
        post.is_owner = True  # In real app verify with JWT
    
    return posts'''

new_get_posts = '''@app.get("/api/posts", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    
    # Add info if it's from current user (mock)
    # TEMPORARY FIX: Mark all as NOT owner until proper auth is implemented
    for post in posts:
        post.is_owner = False  # Temporary fix for security
    
    return posts'''

# Reemplazar en el contenido
content = content.replace(old_get_posts, new_get_posts)

# Escribir el nuevo contenido
with open('main.py', 'w') as f:
    f.write(content)

print("✅ Fixed: Posts now marked as NOT owned by default")
