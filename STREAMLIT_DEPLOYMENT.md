# Streamlit Cloud Deployment Guide

## Overview
This guide provides step-by-step instructions to deploy the HealthAI-ComfyUI-Suite to Streamlit Cloud using Gemini API instead of Pinecone.

## Prerequisites
- GitHub account with access to the HealthAI-ComfyUI-Suite repository
- Gemini API key (free tier available at https://makersuite.google.com/app/apikey)
- Streamlit Cloud account (https://streamlit.io/cloud)

## Step 1: Get Your Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Select "Create API key in new project" or choose existing project
4. Copy the generated API key
5. Keep it safe - you'll need it in the next steps

## Step 2: Deploy to Streamlit Cloud

### Option A: Using "Open in Streamlit" Button (Easiest)
1. Go to the repository homepage
2. Click the "Open in Streamlit" button
3. Sign in with your GitHub account
4. Proceed to Step 3

### Option B: Manual Deployment
1. Go to https://share.streamlit.io/
2. Click "New app"
3. Select GitHub as repository source
4. Enter: `akashBv6680/HealthAI-ComfyUI-Suite`
5. Set Branch to: `main`
6. Set Main file path to: `app/main.py`
7. Click "Deploy"
8. Proceed to Step 3

## Step 3: Configure Secrets

1. Go to your deployed app on Streamlit Cloud
2. Click the menu (≡) in the top right
3. Select "Settings"
4. Click "Secrets"
5. Paste the following in the secrets editor:

```
# Gemini API Configuration
GEMINI_API_KEY = "your_gemini_api_key_here"

# ComfyUI Configuration (optional - for image generation)
COMFYUI_API_URL = "http://localhost:8188"

# Optional API Keys
# OPENAI_API_KEY = "your_openai_key_here"
# AZURE_SPEECH_KEY = "your_azure_speech_key_here"
```

6. Replace `your_gemini_api_key_here` with your actual Gemini API key
7. Click "Save"

## Step 4: Verify Deployment

1. Your app will automatically redeploy with the new secrets
2. Wait for the deployment to complete (check the status in top right)
3. Once deployment is done, your app should display without the "Gemini API Key not found" error
4. You can now use the HealthAI Suite!

## Troubleshooting

### "Gemini API Key not found in secrets"
- Ensure the secret key is exactly `GEMINI_API_KEY` (case-sensitive)
- Go back to Settings > Secrets and verify the key is saved
- Wait a few seconds for the app to reload

### App crashes or errors
- Check the logs by clicking the menu (≡) > "View logs"
- Ensure all dependencies in requirements.txt are compatible
- Verify your Gemini API key is valid at https://makersuite.google.com/app/apikey

### Rate limiting
- Free Gemini API tier has usage limits
- For production use, consider upgrading to a paid plan

## Features
- Multi-agent orchestration with LangGraph
- Medical knowledge retrieval with Gemini AI
- ComfyUI visual generation (requires self-hosted ComfyUI server)
- Multilingual TTS support
- Real-time patient risk assessment

## Configuration Options

You can add more secrets in Streamlit Cloud as needed:

| Secret Key | Purpose | Required |
|-----------|---------|----------|
| GEMINI_API_KEY | Gemini API access | Yes |
| COMFYUI_API_URL | ComfyUI server URL | No (for image generation) |
| OPENAI_API_KEY | OpenAI API access | No |
| AZURE_SPEECH_KEY | Azure TTS service | No |
| TTS_LANGUAGE | TTS language code | No (default: ta for Tamil) |

## Support

For issues or questions:
1. Check the GitHub Issues: https://github.com/akashBv6680/HealthAI-ComfyUI-Suite/issues
2. Review the main README.md for technical details
3. Check Streamlit documentation: https://docs.streamlit.io/

## Next Steps

1. **Local Development**: Run `streamlit run app/main.py` locally to test changes
2. **Add ComfyUI**: Set up a self-hosted ComfyUI server and configure COMFYUI_API_URL
3. **Database Setup**: Configure PostgreSQL for clinic data persistence
4. **Custom Workflows**: Add your own medical workflows and prompts

## Notes

- The repository has been updated to use Gemini API instead of Pinecone for RAG
- Free Gemini API tier supports 60 requests per minute
- For production use, ensure proper API quotas and error handling
