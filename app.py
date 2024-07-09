from wtf import create_app

app = create_app()
print("App created successfully")
print(f"App routes: {app.url_map}")

if __name__ == '__main__':
    app.run(debug=True)
else:
    print("Warning: app.py is being imported, not run directly")