# Django-Api

# Account Token Authentication

# Account api Urls

app_name = 'account'

urlpatterns = [
	path('properties', account_properties_view, name="properties"),
	path('properties/update', update_account_view, name="update"),
	path('login', obtain_auth_token, name="login"),
	path('register', registration_view, name="register"),
]


# Student Expert System Api Urls

app_name = 'studentexpertsystem'

urlpatterns = [
    path('groups/', groups_list),
    path('courses/', courses_list),
    path('boards/',boards_list),
    path("detail_model/",detail_model_view)
 
]
