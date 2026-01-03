# Netlify Deployment Checklist

## ✅ Pre-Deployment Checklist

### Files Created/Modified
- [x] `netlify.toml` - Netlify configuration
- [x] `netlify/functions/server.py` - Serverless function handler
- [x] `requirements.txt` - Updated with `serverless-wsgi`
- [x] `.netlifyignore` - Excludes unnecessary files
- [x] `app.py` - Updated for serverless environment support
- [x] `NETLIFY_DEPLOYMENT.md` - Deployment guide

### Configuration
- [x] Build command: `pip install -r requirements.txt`
- [x] Publish directory: `.`
- [x] Functions directory: `netlify/functions`
- [x] Static files routing configured
- [x] Security headers configured

## 🚀 Deployment Steps

1. **Commit all changes**
   ```bash
   git add .
   git commit -m "Configure for Netlify deployment"
   git push
   ```

2. **Connect to Netlify**
   - Go to https://app.netlify.com
   - Click "Add new site" → "Import an existing project"
   - Connect your Git repository

3. **Set Environment Variables** (in Netlify Dashboard)
   - `SECRET_KEY` - Generate a strong random key
   - `NETLIFY=true`
   - `FLASK_ENV=production`
   - `DATABASE_URL` - (Optional, for cloud database)

4. **Deploy**
   - Netlify will auto-detect settings from `netlify.toml`
   - Click "Deploy site"
   - Monitor build logs

5. **Verify Deployment**
   - Check that site loads
   - Test login functionality
   - Test static file serving
   - Check function logs for errors

## ⚠️ Important Notes

### Database Limitations
- SQLite in `/tmp` won't persist between function invocations
- **For production**: Use PostgreSQL, MySQL, or MongoDB
- Update `DATABASE_URL` environment variable

### File Upload Limitations
- Files in `/tmp/uploads` won't persist
- **For production**: Use S3, Cloudinary, or Netlify Blob Storage

### Testing
- Use `netlify dev` to test locally
- Check function logs in Netlify Dashboard
- Monitor build logs for errors

## 🔧 Troubleshooting

### Build Fails
- Check Python version (should be 3.11)
- Verify all dependencies in `requirements.txt`
- Check build logs for specific errors

### Function Errors
- Check function logs in Netlify Dashboard
- Verify `serverless-wsgi` is installed
- Ensure all imports are correct

### Static Files Not Loading
- Verify `static/` is in `included_files`
- Check redirect rules in `netlify.toml`

## 📚 Additional Resources

- See `NETLIFY_DEPLOYMENT.md` for detailed guide
- Netlify Docs: https://docs.netlify.com
- serverless-wsgi: https://github.com/logandk/serverless-wsgi

