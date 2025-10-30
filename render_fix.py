import re

with open('main.py', 'r') as f:
    content = f.read()

# Encontrar y reemplazar todo desde if __name__ == "__main__" hasta el final
new_content = re.sub(
    r'if __name__ == "__main__":.*',
    '''if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        access_log=False
    )''',
    content,
    flags=re.DOTALL
)

with open('main.py', 'w') as f:
    f.write(new_content)

print("✅ Fixed for Render deployment")
