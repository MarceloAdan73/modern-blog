with open('main.py', 'r') as f:
    content = f.read()

# Reemplazar la parte de get_post individual
old_get_post = '''@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Mark as owned (mock)
    post.is_owner = True
    
    return post'''

new_get_post = '''@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Mark as NOT owned (temporary security fix)
    post.is_owner = False
    
    return post'''

content = content.replace(old_get_post, new_get_post)

with open('main.py', 'w') as f:
    f.write(content)

print("✅ Fixed: Single post also marked as NOT owned")
