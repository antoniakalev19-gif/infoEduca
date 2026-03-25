
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--vwgbt1@#0o1urv+jbbp*4#f62hm#q)9z$$5xi3m0@4jrc3=l4'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # Apps do projeto
    'apps.atividades.apps.AtividadesConfig', # Caminho completo até a classe
    'apps.comunidade.apps.ComunidadeConfig',
    'apps.core.apps.CoreConfig',
    'apps.disciplinas.apps.DisciplinasConfig',
    'apps.professores.apps.ProfessoresConfig',
    'apps.progresso.apps.ProgressoConfig', 
    # Django REST Framework
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]

ROOT_URLCONF = 'infoEduca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'infoEduca.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'pt-br' 
TIME_ZONE = 'America/Bahia' 

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

# No final do seu settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # pasta onde o collectstatic vai juntar tudo
# Caminho onde as fotos serão salvas no seu computador
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_REDIRECT_URL = 'core:home' # Vai para a home após logar
LOGOUT_REDIRECT_URL = 'login'   # Vai para o login após sair
LOGIN_URL = 'login'  # Ou o nome que você deu à sua rota de login
LOGIN_REDIRECT_URL = 'atividades:atividades_home' # Para onde ele vai após logar
LOGIN_REDIRECT_URL = 'redirecionar_usuario'
LOGOUT_REDIRECT_URL = 'login'

# No final do seu InfoEduca/settings.py

JAZZMIN_SETTINGS = {
    # Título da aba no navegador
    "site_title": "InfoEduca Admin",
    
    # Título no painel (em cima do menu lateral)
    "site_header": "InfoEduca",
    
    # Logo da marca (se você tiver um em static/img/logo.png)
    "site_logo": None, 
    
    # Texto de boas-vindas na tela de login
    "welcome_sign": "Bem-vindo ao Painel InfoEduca",
    
    # Copyright no rodapé
    "copyright": "InfoEduca Ltda",

    # Ícones para os apps (usando Font Awesome)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "apps.professores": "fas fa-graduation-cap",
        "apps.disciplinas": "fas fa-book",
        "apps.atividades": "fas fa-tasks",
        "apps.progresso": "fas fa-chart-line",
        "apps.comunidade": "fas fa-comments",
    },
    
    # Deixar o menu lateral sempre aberto
    "navigation_expanded": True,

    # Botão de busca rápida no topo
    "show_sidebar": True,
    "topmenu_links": [
        {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
}

# Opcional: Para mudar as cores (Tema Escuro, Verde, etc)
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
# Configuração de e-mail
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "emails"

EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "seu_email@outlook.com"
EMAIL_HOST_PASSWORD = "sua_senha"