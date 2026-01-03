# Netlify Deployment Guide for MedPro

This guide will help you deploy the MedPro Flask application to Netlify.

## ⚠️ Important Limitations

**Note**: Netlify Functions are serverless, which means:

1. **Database Persistence**: SQLite databases stored in `/tmp` won't persist between function invocations. For production, you should use a cloud database like:
   - PostgreSQL (via Supabase, Neon, or Railway)
   - MySQL (via PlanetScale)
   - MongoDB Atlas

2. **File Uploads**: Files uploaded to `/tmp/uploads` won't persist. Consider using:
   - AWS S3
   - Cloudinary
   - Netlify Blob Storage

3. **Sessions**: Session storage may need adjustment for serverless environments.

## 🚀 Deployment Steps

### 1. Prerequisites

- A GitHub/GitLab/Bitbucket repository with your code
- A Netlify account (free tier works)

### 2. Prepare Your Repository

Make sure your repository includes:
- `netlify.toml` (configuration file)
- `netlify/functions/server.py` (serverless function handler)
- `requirements.txt` (with `serverless-wsgi` included)
- `Training.csv` and `Testing.csv` (for ML model)

### 3. Connect to Netlify

1. Go to [Netlify](https://app.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your Git provider and select your repository
4. Netlify will auto-detect the settings from `netlify.toml`

### 4. Configure Build Settings

Netlify should auto-detect these from `netlify.toml`, but verify:

- **Build command**: `pip install -r requirements.txt`
- **Publish directory**: `.`
- **Functions directory**: `netlify/functions`

### 5. Set Environment Variables

In Netlify Dashboard → Site settings → Environment variables, add:

```
SECRET_KEY=your-super-secret-key-here-change-this
NETLIFY=true
FLASK_ENV=production
```

**For production database** (recommended):
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### 6. Deploy

1. Click "Deploy site"
2. Wait for the build to complete
3. Your site will be live at `https://your-site-name.netlify.app`

## 🔧 Configuration Files

### netlify.toml

This file configures:
- Build settings
- Function routing
- Static file serving
- Security headers

### netlify/functions/server.py

This is the serverless function handler that:
- Adapts Flask to Netlify Functions using `serverless-wsgi`
- Handles all Flask routes
- Initializes the database

## 🐛 Troubleshooting

### Build Fails

1. **Python version**: Ensure `runtime.txt` specifies Python 3.11
2. **Dependencies**: Check that all packages in `requirements.txt` are compatible
3. **File size**: Large files (like CSV files) might need to be in included_files

### Function Errors

1. **Import errors**: Check that all dependencies are in `requirements.txt`
2. **Database errors**: SQLite in `/tmp` won't persist - use a cloud database
3. **Timeout**: Netlify Functions have a 10s timeout (26s on Pro plan)

### Static Files Not Loading

- Ensure `static/` directory is in `included_files` in `netlify.toml`
- Check redirect rules - static files should be served directly

## 📊 Recommended Production Setup

For a production deployment, consider:

1. **Database**: Use PostgreSQL (Supabase, Neon, or Railway)
   ```python
   # Update app.py to use PostgreSQL
   DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://...')
   ```

2. **File Storage**: Use AWS S3 or Cloudinary
   ```python
   # Example with boto3 for S3
   import boto3
   s3 = boto3.client('s3')
   ```

3. **Session Storage**: Use Redis or database-backed sessions
   ```python
   # Use Flask-Session with database backend
   from flask_session import Session
   ```

4. **Environment Variables**: Store secrets in Netlify's environment variables

## 🔒 Security Checklist

- [ ] Change `SECRET_KEY` to a strong random value
- [ ] Use environment variables for all secrets
- [ ] Enable HTTPS (automatic on Netlify)
- [ ] Use a production database (not SQLite)
- [ ] Implement rate limiting
- [ ] Add CORS headers if needed
- [ ] Review and update security headers in `netlify.toml`

## 📝 Additional Resources

- [Netlify Functions Documentation](https://docs.netlify.com/functions/overview/)
- [serverless-wsgi Documentation](https://github.com/logandk/serverless-wsgi)
- [Flask on Serverless](https://flask.palletsprojects.com/en/latest/deploying/)

## 🆘 Support

If you encounter issues:
1. Check Netlify build logs
2. Review function logs in Netlify Dashboard
3. Test locally with Netlify CLI: `netlify dev`

