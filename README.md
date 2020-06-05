# Django-Api

# Account Token Authentication

# Account api Urls
## Usage

```python
app_name = 'account'

urlpatterns = [
	path('properties', account_properties_view, name="properties"),
	path('properties/update', update_account_view, name="update"),
	path('login', obtain_auth_token, name="login"),
	path('register', registration_view, name="register"),
]
```



# Student Expert System Api Urls
## Usage

```python
app_name = 'studentexpertsystem'

urlpatterns = [
    path('groups/', groups_list),
    path('courses/', courses_list),
    path('boards/',boards_list),
    path("detail_model/",detail_model_view)
 
]
```




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
