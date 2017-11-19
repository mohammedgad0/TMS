from django.conf.urls import url ,include
from project import views

#application namespace
app_name = 'ns-project'

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    

    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^add-sheet/$', views.AddSheet, name='add-sheet'),
    url(r'^my_sheet/$', views.MySheet, name='my-sheet'),
    url(r'^all_sheets/$', views.ManagerPage, name='all-sheets'),
    url(r'^dept_sheet/$', views.DeptSheet, name='dept-sheet'),
    url(r'^add_project/$', views.AddProject, name='add-project'),
    url(r'^project_list/$', views.ProjectList, name='project-list'),
    url(r'^project_detail/$', views.ProjectList, name='project-detail'),
    url(r'^project_edit/$', views.ProjectList, name='project-edit'),
    url(r'^project_delete/$', views.ProjectList, name='project-delete'),
    
    url(r'^.*\.html', views.gentella_html, name='gentella'),
]
