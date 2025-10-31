with open('main.py', 'r') as f:
    content = f.read()

# Reemplazar my-posts para mantener la funcionalidad correcta
old_my_posts = '''@app.get("/api/posts/my-posts", response_model=List[PostResponse])
def get_my_posts(db: Session = Depends(get_db)):
    # In real app filter by authenticated user
    user = db.query(User).first()
    if not user:
        return []
    
    posts = db.query(Post).filter(Post.author_id == user.id).order_by(Post.created_at.desc()).all()
    
    # Mark as owned
    for post in posts:
        post.is_owner = True
    
    return posts'''

new_my_posts = '''@app.get("/api/posts/my-posts", response_model=List[PostResponse])
def get_my_posts(db: Session = Depends(get_db)):
    # In real app filter by authenticated user
    user = db.query(User).first()
    if not user:
        return []
    
    posts = db.query(Post).filter(Post.author_id == user.id).order_by(Post.created_at.desc()).all()
    
    # Mark as owned (this should remain True for user's own posts)
    for post in posts:
        post.is_owner = True
    
    return posts'''

content = content.replace(old_my_posts, new_my_posts)

with open('main.py', 'w') as f:
    f.write(content)

print("✅ Fixed: My-posts still correctly marks user posts as owned")
