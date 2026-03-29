"""
FastAPI Entry Point with Frappe-Inspired Architecture - FIXED
"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import importlib.util
import os

app = FastAPI(title="My FastAPI App")

# Directories
BASE_DIR = Path(__file__).resolve().parent
APP_DIR = BASE_DIR / "app"
WWW_DIR = APP_DIR / "www"
TEMPLATES_DIR = APP_DIR / "templates"
PUBLIC_DIR = APP_DIR / "public"

# ✅ FIX: Point to app/ root so Jinja2 can find both templates/ and www/
templates = Jinja2Templates(directory=str(APP_DIR))

# Mount Static Files
app.mount("/public", StaticFiles(directory=str(PUBLIC_DIR)), name="public")

# App configuration
app_config = {
    "app_name": "My FastAPI App",
    "brand_html": '<span class="brand">My App</span>',
    "year": 2024,
    "app_config": {},  # For window.appConfig in JS
}

def is_safe_path(path: str) -> bool:
    """Security: Prevent directory traversal"""
    if not path:
        return True
    if '..' in path or path.startswith('.') or os.path.isabs(path):
        return False
    return True

def load_page_module(page_path: Path) -> dict:
    """Load page-specific Python module (Frappe-style get_context)"""
    context = {}
    py_file = page_path.with_suffix('.py')
    
    if py_file.exists():
        try:
            spec = importlib.util.spec_from_file_location("page_module", py_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'get_context'):
                context = module.get_context(context)
        except Exception as e:
            print(f"⚠️ Error loading {py_file}: {e}")
    
    return context

def find_page_files(page: str) -> dict:
    """Find HTML, CSS, JS, and PY files for a page"""
    files = {'html': None, 'css': None, 'js': None, 'py': None}
    
    if not page or page == '/':
        page = 'index'
    
    # Check for direct file match
    for ext in ['.html', '.css', '.js', '.py']:
        file_path = WWW_DIR / f"{page}{ext}"
        if file_path.exists():
            files[ext[1:]] = file_path
    
    # Check for folder/index files
    if not files['html']:
        folder_path = WWW_DIR / page
        if folder_path.exists() and folder_path.is_dir():
            for ext in ['.html', '.css', '.js', '.py']:
                index_file = folder_path / f"index{ext}"
                if index_file.exists():
                    files[ext[1:]] = index_file
    
    return files

@app.api_route("/{page:path}", methods=["GET", "POST"])
async def frappe_router(request: Request, page: str = ""):
    """Frappe-style router for www folder"""
    
    if not is_safe_path(page):
        raise HTTPException(status_code=404, detail="Not Found")
    
    page_files = find_page_files(page)
    
    if not page_files['html']:
        raise HTTPException(status_code=404, detail="Page Not Found")
    
    # Load page context from .py file
    context = load_page_module(page_files['html'])
    
    # Add global config
    context.update(app_config)
    context['request'] = request
    
    # Set paths for page-specific assets
    if page_files['css']:
        context['page_css'] = f"/public{page_files['css'].relative_to(APP_DIR)}"
    if page_files['js']:
        context['page_js'] = f"/public{page_files['js'].relative_to(APP_DIR)}"
    
    # Handle POST requests
    if request.method == "POST":
        form_data = await request.form()
        context['form_data'] = dict(form_data)
        
        py_file = page_files['html'].with_suffix('.py')
        if py_file.exists():
            try:
                spec = importlib.util.spec_from_file_location("page_module", py_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'on_form_submit'):
                    result = module.on_form_submit(context['form_data'])
                    if result:
                        context['form_success'] = result.get('success', False)
                        context['form_message'] = result.get('message', '')
            except Exception as e:
                print(f"⚠️ Form submit error: {e}")
    
    # ✅ FIX: Use TemplateResponse for ALL HTML (not standalone Template)
    try:
        template_name = str(page_files['html'].relative_to(APP_DIR))
        return templates.TemplateResponse(
            name=template_name,
            context=context,
            request=request
        )
    except Exception as e:
        print(f"❌ Template error: {e}")
        raise HTTPException(status_code=500, detail=f"Template error: {str(e)}")

@app.exception_handler(404)
async def custom_404(request: Request, exc):
    return templates.TemplateResponse(
        name="templates/404.html",
        context={**app_config, "request": request},
        request=request,
        status_code=404
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
