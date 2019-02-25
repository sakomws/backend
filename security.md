Disable admin access:
```
ADMIN_ENABLED = False
```
Then in your urls.py:
```
if settings.ADMIN_ENABLED:
    urlpatterns += patterns('',
        (r'^admin/(.*)', include(admin.site.urls)),
        # ..maybe other stuff you want to be dev-only, etc...
        )
```

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
