# Deployment Notes

## In-Memory Processing

This application processes CSV files entirely in memory without saving them to disk. This design choice offers several advantages:

### Benefits

1. **No File System Required**
   - Works on platforms with restricted file system access
   - Perfect for serverless deployments (AWS Lambda, Google Cloud Functions, etc.)
   - Compatible with GitHub Pages (with backend), Heroku, Railway, etc.

2. **No Cleanup Required**
   - Files are automatically cleared when the session ends
   - No orphaned files accumulating on disk
   - No background cleanup jobs needed

3. **Better Security**
   - Files don't persist on the server
   - No risk of sensitive data remaining on disk
   - Each user's data is isolated in their session

4. **Stateless Architecture**
   - Easy to scale horizontally
   - No shared file system needed between instances
   - Works well with load balancers

### How It Works

1. **File Upload**: User uploads CSV via web form
2. **Memory Loading**: File is read into memory as BytesIO stream
3. **Validation**: CSV structure is validated
4. **Session Storage**: Data is converted to CSV string and stored in Flask session
5. **Analysis**: Data is read from session as StringIO stream for analysis
6. **Auto-Cleanup**: Session data is cleared when user navigates away or session expires

### Session Configuration

The application uses Flask's built-in session management. For production:

1. Set a strong secret key in `app.py`:
   ```python
   app.secret_key = 'your-production-secret-key-here'
   ```

2. Consider using server-side sessions for large files:
   - Flask-Session with Redis backend
   - Flask-Session with filesystem backend (if available)

### Limitations

- **Session Size**: Large CSV files may exceed session storage limits (usually 4KB for cookies)
- **Memory Usage**: Multiple concurrent users will consume server RAM
- **Session Timeout**: Users must complete analysis before session expires

### Recommendations for Production

1. **Use server-side sessions** for files > 1MB
2. **Set session timeout** appropriately (e.g., 30 minutes)
3. **Monitor memory usage** and set appropriate limits
4. **Consider Redis** for session storage in multi-instance deployments

## Deployment Platforms

### Heroku
```bash
# Procfile
web: python app.py
```

### Railway
No additional configuration needed. Railway auto-detects Flask apps.

### AWS Lambda (with Zappa)
Works out of the box with Zappa for serverless deployment.

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Environment Variables

For production, set these environment variables:
- `FLASK_SECRET_KEY`: Your secret key
- `FLASK_ENV`: Set to `production`
- `MAX_CONTENT_LENGTH`: Maximum file size in bytes (default: 16MB)
